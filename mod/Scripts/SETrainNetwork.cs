/*
 * SETrainNetwork.cs
 *
 * Mod/Client side networking code to allow the mod to communicate
 * with the SE Train server
 */

using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;

using Sandbox.ModAPI;

using VRage.Game;
using VRage.Utils;

namespace SETrain {
  public class SETrainNetworkHandler {
    // Configuration constants
    private const string SERVER_IP = "127.0.0.1";
    private const int SERVER_PORT = 11000;
    private const int LISTEN_PORT = 11001;

    // Local variables
    private UdpClient m_Udp;
    private IPEndPoint m_SeverEndpoint;
    private bool m_Running = true;

    // Buffer
    private List<string> m_Buffer = new List<string>();
    private readonly object m_BufferLock = new object();
    
    public SETrainNetworkHandler() {
      // Initialize server communications
      m_SeverEndpoint = new IPEndPoint(IPAddress.Parse(SERVER_IP), SERVER_PORT);

      // Initialize UDP listener
      m_Udp = new UdpClient(LISTEN_PORT);
      m_Udp.Client.ReceiveTimeout = 100;

      // Background listener
      MyAPIGateway.Parallel.StartBackground(listenLoop);
    }

    private void listenLoop() {
      while (m_Running) {
        try {
          IPEndPoint remoteEndpoint = new IPEndPoint(IPAddress.Any, LISTEN_PORT);
          byte[] bytes = m_Udp.Receive(ref remoteEndpoint);
          string raw = Encoding.UTF8.GetString(bytes);

          lock (m_BufferLock) {
            m_Buffer.Add(raw);
          }
        } 
        catch (SocketException) {}
        catch (Exception e) {
          MyLog.Default.WriteLine($"SETrain: Network Error: {e.Message}");
        }
      }
    }

    public Dictionary<string, string> poll() {
      string raw = null;

      lock (m_BufferLock) {
        if (m_Buffer.Count > 0) {
          raw = m_Buffer[0];
          m_Buffer.RemoveAt(0);
        }
      }

      if (string.IsNullOrEmpty(raw)) return new Dictionary<string, string>();

      try {
        return MyAPIGateway.Utilities.SerializeFromJSON<Dictionary<string, string>>(raw);
      } catch (Exception e) {
        MyLog.Default.WriteLine($"SETrain: JSON Parse Error: {e.Message}");
        return new Dictionary<string, string>();
      }
    }

          

    // Deinitializer; destroys UDP context on game unload
    public void destroy() {
      m_Udp?.close();
    }
  }
}
