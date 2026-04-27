/*
 * SE Train - A Train Mod for Space Engineers
 *
 * SETrain.cs - Main mod entry point
 * Author: Surge
 * Version: 1.0
 */

// All wip

namespace SETrain {

  [MySessionComponentDescriptor(MyUpdateOrder.AfterSimulation)]
  public class ModEntry : MySessionComponentBase {

    private SETrainNetworkHandler m_NetworkHandler;

    public override void LoadData() {
      m_NetworkHandler = new SETrainNetworkHandler();
    }

    public override void UpdateAfterSimulation() {
    }

    protected override void UnloadData() {
      m_NetworkHandler.destroy();
    }
  }

}
