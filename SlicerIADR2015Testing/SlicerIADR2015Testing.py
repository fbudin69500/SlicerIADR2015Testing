import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import urllib

#
# SlicerIADR2015Testing
#

class SlicerIADR2015Testing(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "IADR2015 Download Data"
    self.parent.categories = ["Testing"]
    self.parent.dependencies = []
    self.parent.contributors = ["Francois Budin (UNC)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    This example downloads data for the IADR2015 workshop
    """
    self.parent.acknowledgementText = """
""" # replace with organization, grant and thanks.

#
# SlicerIADR2015TestingWidget
#

class SlicerIADR2015TestingWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    self.logic = SlicerIADR2015TestingLogic()
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
    self.step1Button.toolTip = "Download step 1 data - DICOM"
    self.step1Button.enabled = False
    parametersFormLayout.addRow(self.step1Button)
    #Step 2
    self.step2Button = qt.QPushButton("Download Step 2 data")
    self.step2Button.toolTip = "Download step 2 data - To approximate manually"
    self.step2Button.enabled = True
    parametersFormLayout.addRow(self.step2Button)
    #Step 3
    self.step3Button = qt.QPushButton("Download Step 3 data")
    self.step3Button.toolTip = "Download step 3 data - To do Segmentation"
    self.step3Button.enabled = True
    parametersFormLayout.addRow(self.step3Button)
    #Step 4
    self.step4Button = qt.QPushButton("Download Step 4 data")
    self.step4Button.toolTip = "Download step 4 data - To do voxel-based registration"
    self.step4Button.enabled = True
    parametersFormLayout.addRow(self.step4Button)
    #Step 5
    self.step5Button = qt.QPushButton("Download Step 5 data")
    self.step5Button.toolTip = "Download step 5 data - To make models"
    self.step5Button.enabled = True
    parametersFormLayout.addRow(self.step5Button)
    #Step 6
    self.step6Button = qt.QPushButton("Download Step 6 data")
    self.step6Button.toolTip = "Download step 6 data - To compute colormaps"
    self.step6Button.enabled = True
    parametersFormLayout.addRow(self.step6Button)
    #Step 7
    self.step7Button = qt.QPushButton("Download Step 7 data")
    self.step7Button.toolTip = "Download step 7 data - Quantification"
    self.step7Button.enabled = True
    parametersFormLayout.addRow(self.step7Button)
    #Step 8
    self.step8Button = qt.QPushButton("Download Step 8 data")
    self.step8Button.toolTip = "Download step 8 data - Extra material"
    self.step8Button.enabled = True
    parametersFormLayout.addRow(self.step8Button)

    # connections
    self.step1Button.connect('clicked(bool)', self.onStep1Button)
    self.step2Button.connect('clicked(bool)', self.onStep2Button)
    self.step3Button.connect('clicked(bool)', self.onStep3Button)
    self.step4Button.connect('clicked(bool)', self.onStep4Button)
    self.step5Button.connect('clicked(bool)', self.onStep5Button)
    self.step6Button.connect('clicked(bool)', self.onStep6Button)
    self.step7Button.connect('clicked(bool)', self.onStep7Button)
    self.step8Button.connect('clicked(bool)', self.onStep8Button)


    # Add vertical spacer
    self.layout.addStretch(1)

  def cleanup(self):
    pass

  def delayDisplay(self,message,msec=1000):
    #
    # logic version of delay display
    #
    print(message)
    self.info = qt.QDialog()
    self.infoLayout = qt.QVBoxLayout()
    self.info.setLayout(self.infoLayout)
    self.label = qt.QLabel(message,self.info)
    self.infoLayout.addWidget(self.label)
    qt.QTimer.singleShot(msec, self.info.close)
    self.info.exec_()

  def onStep1Button(self):
    self.logic.runStep1()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep2Button(self):
    self.logic.runStep2()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep3Button(self):
    self.logic.runStep3()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep4Button(self):
    self.logic.runStep4()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep5Button(self):
    self.logic.runStep5()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep6Button(self):
    self.logic.runStep6()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep7Button(self):
    answer,filesNotLoaded=self.logic.runStep7()
    print("main:%s"%(filesNotLoaded))
    if filesNotLoaded:
      self.ListFilesQt = qt.QDialog()
      self.ListFilesQtLayout = qt.QVBoxLayout()
      self.ListFilesQt.setLayout(self.ListFilesQtLayout)
      text="Files downloaded but not loaded in Slicer:"
      for s in filesNotLoaded:
        text+="\n"+s
      self.ListFilesQtlabel = qt.QLabel(text,self.ListFilesQt)
      self.ListFilesQtlabel.setTextInteractionFlags(qt.Qt.TextSelectableByMouse)
      self.ListFilesQtLayout.addWidget(self.ListFilesQtlabel)
      self.ListFilesQt.show()
    self.delayDisplay('Finished with download and loading',2000)
  def onStep8Button(self):
    self.logic.runStep8()
    self.delayDisplay('Finished with download and loading',2000)

#
# SlicerIADR2015TestingLogic
#

class SlicerIADR2015TestingLogic(ScriptedLoadableModuleLogic):
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
      fileList=[]
      for url,name,loader in downloads:
        filePath = slicer.app.temporaryPath + '/' + name
        realURL = rootURL + url
        if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
            logging.info('Requesting download %s from %s...\n' % (name, realURL))
            urllib.urlretrieve(realURL, filePath)
        fileList.append(filePath)
        if loader:
            logging.info('Loading %s...' % (name,))
            loader(filePath)
        else:
            logging.info( 'File downloaded here: %s' %filePath )
      return fileList

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
    logging.info('Step 2 started')
    downloads = (
          ('182296', 'Patient_ScanT1.gipl.gz', slicer.util.loadVolume),
          ('182297', 'Patient_ScanT2.gipl.gz', slicer.util.loadVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Step 2 completed')
    return True

  def runStep3(self):
    """
    Run the actual algorithm
    """
    logging.info('Step 3 started')
    downloads = (
          ('182298', 'Patient_ScanT1.gipl.gz', slicer.util.loadVolume),
          ('182299', 'Patient_ScanT2_approx.gipl.gz', slicer.util.loadVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Step 4 completed')
    return True

  def runStep4(self):
    """
    Run the actual algorithm
    """
    logging.info('Step 4 started')
    downloads = (
          ('182300', 'Patient_MaskCBT2_approxCB.gipl.gz', slicer.util.loadLabelVolume),
          ('182301', 'Patient_ScanT1.gipl.gz', slicer.util.loadLabelVolume),
          ('182302', 'Patient_ScanT2_approxCB.gipl.gz', slicer.util.loadLabelVolume),
          ('182303', 'Patient_SegmSkullT1.gipl.gz', slicer.util.loadLabelVolume),
          ('182304', 'Patient_SegmSkullT2_ApproxCB.gipl.gz', slicer.util.loadLabelVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Step 4 completed')
    return True

  def runStep5(self):
    """
    Run the actual algorithm
    """
    logging.info('Step 5 started')
    downloads = (
          ('182305', 'Patient_SegmSkullT1.gipl.gz', slicer.util.loadLabelVolume),
          ('182306', 'Patient_SegmT2_regCB.gipl.gz', slicer.util.loadLabelVolume),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Step 5 completed')
    return True

  def runStep6(self):
    """
    Run the actual algorithm
    """
    logging.info('Step 6 started')
    downloads = (
          ('182307', 'Patient_ModelT1_skull.vtk', slicer.util.loadModel),
          ('182308', 'Patient_ModelT2_skull_regCB.vtk', slicer.util.loadModel),
                )
    self.DownloadAndLoad(downloads)
    logging.info('Step 6 completed')
    return True

  def runStep7(self):
    """
    Run the actual algorithm
    """
    logging.info('Step 7 started')
    downloads = (
          ('182309', 'Model_Skull_T1_T2.vtk', slicer.util.loadModel),
          ('182310', 'Model_Skull_T1_T2_1_ROI.csv',None),
          ('182311', 'Model_Skull_T1_T2_with_ROI.vtk', slicer.util.loadModel),
                )
    fileList=self.DownloadAndLoad(downloads)
    filesNotLoaded=[]
    for x in fileList:
      if x.endswith(".csv"):
        filesNotLoaded.append(x)
    logging.info('Step 7 completed')
    return (True,filesNotLoaded)

  def runStep8(self):
    """
    Run the actual algorithm
    """
    logging.info('Step 8 started')
    downloads = (
          ('182312', 'Model_CB_Patient_T1.vtk', slicer.util.loadModel),
          ('182313', 'Model_CB_Patient_T2.vtk', slicer.util.loadModel),
          ('182314', 'Model_MD_Patient_T1.vtk', slicer.util.loadModel),
          ('182315', 'Model_MD_Reg_CB_Patient_T2.vtk', slicer.util.loadModel),
          ('182316', 'Model_MX_Patient_T1.vtk', slicer.util.loadModel),
          ('182317', 'Model_MX_Reg_CB_Patient_T2.vtk', slicer.util.loadModel),

                )
    self.DownloadAndLoad(downloads)
    logging.info('Step 8 completed')
    return True

class SlicerIADR2015TestingTest(ScriptedLoadableModuleTest):
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

