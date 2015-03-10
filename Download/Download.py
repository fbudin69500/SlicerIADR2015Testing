import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import urllib

#
# Download
#

class Download(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "IADR2015 Download Data" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Testing"]
    self.parent.dependencies = []
    self.parent.contributors = ["Francois Budin (UNC)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    This example downloads data for the IADR2015 workshop
    """
    self.parent.acknowledgementText = """
""" # replace with organization, grant and thanks.

#
# DownloadWidget
#

class DownloadWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    self.logic = DownloadLogic()
    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #Step 1 - DICOM conversion
    self.step1Button = qt.QPushButton("Download Step 1 data")
    self.step1Button.toolTip = "Download step 1 data"
    self.step1Button.enabled = False
    parametersFormLayout.addRow(self.step1Button)
    #Step 2
    self.step2Button = qt.QPushButton("Download Step 2 data")
    self.step2Button.toolTip = "Download step 2 data"
    self.step2Button.enabled = True
    parametersFormLayout.addRow(self.step2Button)
    #Step 3
    self.step3Button = qt.QPushButton("Download Step 3 data")
    self.step3Button.toolTip = "Download step 3 data"
    self.step3Button.enabled = True
    parametersFormLayout.addRow(self.step3Button)
    #Step 4
    self.step4Button = qt.QPushButton("Download Step 4 data")
    self.step4Button.toolTip = "Download step 4 data"
    self.step4Button.enabled = True
    parametersFormLayout.addRow(self.step4Button)
    #Step 5
    self.step5Button = qt.QPushButton("Download Step 5 data")
    self.step5Button.toolTip = "Download step 5 data"
    self.step5Button.enabled = True
    parametersFormLayout.addRow(self.step5Button)
    #Step 6
    self.step6Button = qt.QPushButton("Download Step 6 data")
    self.step6Button.toolTip = "Download step 6 data"
    self.step6Button.enabled = True
    parametersFormLayout.addRow(self.step6Button)

    # connections
    self.step1Button.connect('clicked(bool)', self.onStep1Button)
    self.step2Button.connect('clicked(bool)', self.onStep2Button)
    self.step3Button.connect('clicked(bool)', self.onStep3Button)
    self.step4Button.connect('clicked(bool)', self.onStep4Button)
    self.step5Button.connect('clicked(bool)', self.onStep5Button)
    self.step6Button.connect('clicked(bool)', self.onStep6Button)


    # Add vertical spacer
    self.layout.addStretch(1)

  def cleanup(self):
    pass

  def onStep1Button(self):
    self.logic.runStep1()
    slicer.util.delayDisplay('Finished with download and loading',2000)
  def onStep2Button(self):
    self.logic.runStep2()
    slicer.util.delayDisplay('Finished with download and loading',2000)
  def onStep3Button(self):
    self.logic.runStep3()
    slicer.util.delayDisplay('Finished with download and loading',2000)
  def onStep4Button(self):
    self.logic.runStep4()
    slicer.util.delayDisplay('Finished with download and loading',2000)
  def onStep5Button(self):
    self.logic.runStep5()
    slicer.util.delayDisplay('Finished with download and loading',2000)
  def onStep6Button(self):
    self.logic.runStep6()
    slicer.util.delayDisplay('Finished with download and loading',2000)

#
# DownloadLogic
#

class DownloadLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def DownloadAndLoad(self, downloads):
      rootURL = 'http://slicer.kitware.com/midas3/download?items='
      for url,name,loader in downloads:
        filePath = slicer.app.temporaryPath + '/' + name
        realURL = rootURL + url
        if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
            logging.info('Requesting download %s from %s...\n' % (name, realURL))
            urllib.urlretrieve(realURL, filePath)
        if loader:
            logging.info('Loading %s...' % (name,))
            loader(filePath)

  def runStep1(self):
    """
    Run the actual algorithm
    """
    logging.info('Nothing to be done')
    return True

  def runStep2(self):
    """
    Run the actual algorithm
    """
    logging.info('Processing started')
    downloads = (
          ('181114', 'Patient_ScanT1.nii.gz', slicer.util.loadVolume),
          ('181115', 'Patient_ScanT2_without_approx.nii.gz', slicer.util.loadVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Processing completed')
    return True

  def runStep3(self):
    """
    Run the actual algorithm
    """
    logging.info('Processing started')
    downloads = (
          ('181116', 'Patient_ScanT2_registered.nii.gz', slicer.util.loadVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Processing completed')
    return True

  def runStep4(self):
    """
    Run the actual algorithm
    """
    logging.info('Processing started')
    downloads = (
          ('181117', 'Patient_SegmCBT1.nii.gz', slicer.util.loadLabelVolume),
          ('181118', 'Patient_SegmCBT2.nii.gz', slicer.util.loadLabelVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Processing completed')
    return True

  def runStep5(self):
    """
    Run the actual algorithm
    """
    logging.info('Processing started')
    downloads = (
          ('181119', 'PPatient_SegmMDT1.nii.gz', slicer.util.loadLabelVolume),
          ('181120', 'Patient_SegmMXT1.nii.gz', slicer.util.loadLabelVolume),
          ('181121', 'Output_RegCB_SCAN_Patient_T2.nii.gz', slicer.util.loadVolume),
          ('181122', 'Output_RegCB_SegBC_Patient_T2.nii.gz', slicer.util.loadLabelVolume),
          ('181123', 'Output_RegCB_SegmMD_Patient_T2.nii.gz', slicer.util.loadLabelVolume),
          ('181124', 'Output_RegCB_SegmMX_Patient_T2.nii.gz', slicer.util.loadLabelVolume),
          ('181125', 'Registration_Matrix_Patient_RegCB.tfm', slicer.util.loadTransform),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Processing completed')
    return True

  def runStep6(self):
    """
    Run the actual algorithm
    """
    logging.info('Processing started')
    downloads = (
          ('181126', 'Model_CB_Patient_T1.vtk', slicer.util.loadModel),
          ('181127', 'Model_CB_Patient_T2.vtk', slicer.util.loadModel),
          ('181128', 'Model_MD_Patient_T1.vtk', slicer.util.loadModel),
          ('181129', 'Model_MD_Reg_CB_Patient_T2.vtk', slicer.util.loadModel),
          ('181130', 'Model_MX_Patient_T1.vtk', slicer.util.loadModel),
          ('181131', 'Model_MX_Reg_CB_Patient_T2.vtk', slicer.util.loadModel),
          ('181132', 'Model_skull_Patient_T1.vtk', slicer.util.loadModel),
          ('181133', 'Model_skull_Patient_T2.vtk', slicer.util.loadModel),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Processing completed')
    return True

class DownloadTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()

