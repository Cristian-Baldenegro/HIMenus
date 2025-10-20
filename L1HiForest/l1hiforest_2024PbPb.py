### HiForest Configuration
# Input: miniAOD
# Type: data

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_pp_on_PbPb_2024_cff import Run3_pp_on_PbPb_2024
process = cms.Process('HiForest',Run3_pp_on_PbPb_2024)

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 141X, data")

# import subprocess, os
# version = subprocess.check_output(
#     ['git', '-C', os.path.expandvars('$CMSSW_BASE/src'), 'describe', '--tags'])
# if version == '':
#     version = 'no git info'
# process.HiForestInfo.HiForestVersion = cms.string(version)

###############################################################################

# input files

process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring('/store/hidata/HIRun2024B/HIEphemeralZeroBias0/MINIAOD/PromptReco-v2/000/388/769/00000/4c2f4844-8df8-4ad1-9b1b-6b4b93e909b9.root'),
    secondaryFileNames = cms.untracked.vstring(
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/01ec17cf-fc9c-4d3c-b8db-e6961d1d5ccb.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/0b22e368-4ebc-4ba5-90df-841085488070.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/297b955f-d247-442d-aa33-a7280d8fefa2.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/2d38780e-763e-4e7c-94e4-00f3247924bc.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/650b624c-0c65-4d4b-88c1-ee8b201389e2.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/670b6c59-63ee-4d06-93bc-029132838eb7.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/6c9f9f56-e6c2-4166-8d40-1b5f46953035.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/7452ded9-a288-4a05-b856-c0c391584aef.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/74ea10fd-8553-41f8-aebf-87f138bfa578.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/765a36c9-d8b3-47f2-92fe-2cf7fd264a07.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/82599b7a-1e25-419d-9a11-454c96c40951.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/a92959bc-432d-418c-a31e-ca8f3027b833.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/f09315a9-dfb9-48a1-9807-c2dcfdbc9758.root',
'/store/hidata/HIRun2024B/HIEphemeralZeroBias0/RAW/v1/000/388/769/00000/f61b297d-447a-4700-8889-393c06b7afa9.root'
    ),
    dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_gtStage2Digis_*_RECO',
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')


# other shit


# import of standard configurations
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff') # mapper for raw prime
process.load('Configuration.StandardSequences.EndOfProcess_cff')



#Replace GT for running over 2024
from Configuration.AlCa.GlobalTag import GlobalTag
process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")
#process.HcalTPGCoderULUT.LUTGenerationMode = cms.bool(False)
#process.GlobalTag = GlobalTag(process.GlobalTag, '141X_dataRun3_HLT_Candidate_2024_10_20_06_24_01', 'Tag,HcalL1TriggerObjectsRcd,sqlite_file:HcalL1TriggerObjects_2024_ZDC_TEST_B.db')
#process.GlobalTag = GlobalTag(process.GlobalTag, '141X_dataRun3_v6', '')

process.GlobalTag = GlobalTag(process.GlobalTag, '141X_dataRun3_Prompt_v3', '')
#process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

#process.add_(cms.Service("AdaptorConfig", native=cms.untracked.vstring("root")))


## --> only use this starting from 388000
process.es_prefer = cms.ESPrefer('HcalTextCalibrations','es_ascii')
process.es_ascii = cms.ESSource('HcalTextCalibrations',
   input = cms.VPSet(
      cms.PSet(
         object = cms.string('Gains'),
         file   = cms.FileInPath('HeavyIonsAnalysis/Configuration/data/ZDCConditions_1400V/DumpGainsForUpload_AllChannels.txt')
      ),
      cms.PSet(
        object = cms.string('TPChannelParameters'),
        file   = cms.FileInPath('HeavyIonsAnalysis/Configuration/data/ZDCConditions_1400V/DumpTPChannelParameters_Run387473.txt')
      ),
   )
)
## <--
###############################################################################

# Define centrality binning
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root"))

# # edm output for debugging purposes
# process.output = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('HiForestEDM.root'),
#     outputCommands = cms.untracked.vstring(
#         'keep *',
#         )
#     )

# process.output_path = cms.EndPath(process.output)

###############################################################################

# event analysis
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

#process.hiEvtAnalyzer.doCentrality = cms.bool(False)
#process.hiEvtAnalyzer.doHFfilters = cms.bool(False)

# FIXME: Do we have an updated trigger list?
#from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_data_2023_skimmed
#process.hltobject.triggerNames = trigger_list_data_2023_skimmed

process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
################################
# electrons, photons, muons
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doMuons = cms.bool(False)
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.akCs4PFJetSequence_pponPbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.akPu4CaloJetSequence_pponPbPb_data_cff')
process.akPu4CaloJetAnalyzer.doHiJetID = True
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
# muons (FTW)
process.load("HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi")
process.load("HeavyIonsAnalysis.MuonAnalysis.muonAnalyzer_cfi")
###############################################################################

#########################
# ZDC RecHit Producer && Analyzer
#########################
# to prevent crash related to HcalSeverityLevelComputerRcd record
process.load("RecoLocalCalo.HcalRecAlgos.hcalRecAlgoESProd_cfi")
process.load('HeavyIonsAnalysis.ZDCAnalysis.ZDCAnalyzersPbPb_cff')

###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo +
    process.centralityBin +
    process.hiEvtAnalyzer +
#    process.hltanalysis +
    #process.hltobject +
    process.l1object +
    process.trackSequencePbPb +
    process.particleFlowAnalyser +
    process.ggHiNtuplizer +
    process.zdcSequencePbPb +
    process.unpackedMuons +
    process.muonAnalyzer +
    process.akPu4CaloJetAnalyzer
    )

#customisation

# Select the types of jets filled
matchJets = False             # Enables q/g and heavy flavor jet identification in MC 
jetPtMin = 15
jetAbsEtaMax = 2.5

# Choose which additional information is added to jet trees
doHIJetID = True             # Fill jet ID and composition information branches
doWTARecluster = True        # Add jet phi and eta for WTA axis
doBtagging  =  False         # Note that setting to True increases computing time a lot

# 0 means use original mini-AOD jets, otherwise use R value, e.g., 3,4,8
# Add all the values you want to process to the list
# These will create collections of CS subtracted jets (only eta dependent background)
jetLabelsCS = ["4"]

# For this list, give the R-values for flow subtracted CS jets (eta and phi dependent background)
jetLabelsFlowCS = ["4"]

# Combine the two lists such that all selected jets can be easily looped over
# Also add "Flow" tag for the flow jets to distinguish them from non-flow jets
allJetLabels = jetLabelsCS + [flowR + "Flow" for flowR in jetLabelsFlowCS]

# add candidate tagging
from HeavyIonsAnalysis.JetAnalysis.setupJets_PbPb_cff import candidateBtaggingMiniAOD

for jetLabel in allJetLabels:
    candidateBtaggingMiniAOD(process, isMC = False, jetPtMin = jetPtMin, jetCorrLevels = ['L2Relative', 'L2L3Residual'], doBtagging = doBtagging, labelR = jetLabel)

    # setup jet analyzer
    setattr(process,"akCs"+jetLabel+"PFJetAnalyzer",process.akCs4PFJetAnalyzer.clone())
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").jetTag = "selectedUpdatedPatJetsAK"+jetLabel+"PFBtag"
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").jetName = 'akCs'+jetLabel+'PF'
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").matchJets = matchJets
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").matchTag = 'patJetsAK'+jetLabel+'PFUnsubJets'
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").doBtagging = doBtagging
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").doHiJetID = doHIJetID
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").doWTARecluster = doWTARecluster
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").jetPtMin = jetPtMin
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").jetAbsEtaMax = cms.untracked.double(jetAbsEtaMax)
    getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").rParam = 0.4 if jetLabel=="0" else float(jetLabel.replace("Flow",""))*0.1
    if doBtagging:
        getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").pfJetProbabilityBJetTag = cms.untracked.string("pfJetProbabilityBJetTagsAK"+jetLabel+"PFBtag")
        getattr(process,"akCs"+jetLabel+"PFJetAnalyzer").pfUnifiedParticleTransformerAK4JetTags = cms.untracked.string("pfUnifiedParticleTransformerAK4JetTagsAK"+jetLabel+"PFBtag")
    process.forest += getattr(process,"akCs"+jetLabel+"PFJetAnalyzer")

process.pAna = cms.EndPath(process.skimanalysis)

# Additional output definition

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step, process.endjob_step)
process.schedule = cms.Schedule(process.forest,process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)

# add hcal calibrations
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimHcalTP
process = L1TReEmulFromRAWsimHcalTP(process) 

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParamsHI_2023_v0_4_3

#call to customisation function L1TSettingsToCaloParams_2018_v1_4_1 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParamsHI_2023_v0_4_3(process)


# Automatic addition of the customisation function from L1Trigger.Configuration.customiseUtils
from L1Trigger.Configuration.customiseUtils import L1TGlobalMenuXML 

#call to customisation function L1TGlobalMenuXML imported from L1Trigger.Configuration.customiseUtils
process = L1TGlobalMenuXML(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion



# =====================================================================
# add in the zdc analyzer - this writes the digi information to a tree
process.load("RecoLocalCalo.HcalRecAlgos.hcalRecAlgoESProd_cfi")
process.load('HeavyIonsAnalysis.ZDCAnalysis.ZDCAnalyzersPbPb_cff')


# ======================================================================
# ======================================================================
# ======================== add in the emulator =========================
# unpacked etsums
process.l1UpgradeTree.sumZDCTag = cms.untracked.InputTag("gtStage2Digis","EtSumZDC") 
process.l1UpgradeTree.sumZDCToken = cms.untracked.InputTag("gtStage2Digis","EtSumZDC")

# l1 emulator sums
process.l1UpgradeEmuTree.sumZDCTag = cms.untracked.InputTag("etSumZdcProducer")
process.l1UpgradeEmuTree.sumZDCToken = cms.untracked.InputTag("etSumZdcProducer")

# do not change these settings
process.etSumZdcProducer = cms.EDProducer('L1TZDCProducer',
                                          hcalTPDigis = cms.InputTag("simHcalTriggerPrimitiveDigis"),
#                                          hcalTPDigis = cms.InputTag("hcalDigis"),
                                          bxFirst = cms.int32(-2),
                                          bxLast = cms.int32(3)
)

#Via Hannah, for the simHcal collection
process.simHcalTriggerPrimitiveDigis.inputLabel = cms.VInputTag("hcalDigis", "hcalDigis:ZDC")
process.simHcalTriggerPrimitiveDigis.inputUpgradeLabel = cms.VInputTag("hcalDigis", "hcalDigis:ZDC")


process.etSumZdc = cms.Path(process.etSumZdcProducer)
process.schedule.append(process.etSumZdc)
#======================================================================


# input tag replacement needed for raw prime data
#MassReplaceInputTag(process, new="rawPrimeDataRepacker", old="rawDataCollector")

#from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
#MassReplaceInputTag(process, new="rawDataMapperByLabel", old="rawDataCollector")


#input tag needed for regular HI data
#MassReplaceInputTag(process, new="rawDataRepacker", old="rawDataCollector")



#from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
#process.hltfilter = hltHighLevel.clone(
#    HLTPaths = [
#        #"HLT_HIZeroBias_v4",                                                     
#        "HLT_HIMinimumBias_v2",
#    ]
#)
#process.filterSequence = cms.Sequence(
#    process.hltfilter
#)
#
#process.superFilterPath = cms.Path(process.filterSequence)
#process.skimanalysis.superFilters = cms.vstring("superFilterPath")
#
#for path in process.paths:
#    getattr(process, path)._seq = process.filterSequence * getattr(process,path)._seq
