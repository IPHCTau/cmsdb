# vv.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022
# ID: 181505XX

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn



cpn.add_dataset(
    name='ww_dl_powheg',
    id=18150501,
    is_data=False,
    processes=[procs.ww_dl],
    keys=['/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=10,
    n_events=12732644.0, # this n_events is the gensumwt
    aux={'n_events': 12735192} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='ww_sl_powheg',
    id=18150502,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=43,
    n_events=53661178.0, # this n_events is the gensumwt
    aux={'n_events': 53671760} # n_events in aux is the nEvents produced
)


cpn.add_dataset(
    name='wz_wlnu_zll_powheg',
    id=18150511,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=13,
    n_events=2791528.0, # this n_events is the gensumwt
    aux={'n_events': 2797132} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wz_wqq_zll_powheg',
    id=18150512,
    is_data=False,
    processes=[procs.wz_wqq_zll],
    keys=['/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'], #noqa
    n_files=32,
    n_events=8432772.0, # this n_events is the gensumwt
    aux={'n_events': 8441558} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wz_wlnu_zqq_powheg',
    id=18150513,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=9,
    n_events=17619082.0, # this n_events is the gensumwt
    aux={'n_events': 17626624} # n_events in aux is the nEvents produced
)


cpn.add_dataset(
    name='zz_zqq_zll_powheg',
    id=18150521,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'], #noqa
    n_files=35,
    n_events=29478956.0, # this n_events is the gensumwt
    aux={'n_events': 29662670} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='zz_zll_znunu_powheg',
    id=18150522,
    is_data=False,
    processes=[procs.zz_zll_znunu],
    keys=['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=53,
    n_events=29249225.0, # this n_events is the gensumwt
    aux={'n_events': 29313363} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='zz_zll_zll_powheg',
    id=18150523,
    is_data=False,
    processes=[procs.zz_zll_zll],
    keys=['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=88,
    n_events=28778338.0, # this n_events is the gensumwt
    aux={'n_events': 29079492} # n_events in aux is the nEvents produced
)



cpn.add_dataset(
    name='www_amcatnlo',
    id=18150531,
    is_data=False,
    processes=[procs.www],
    keys=['/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM',
          '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM'],
    n_files=2 + 16,
    n_events=408136.0, # this n_events is the gensumwt
    aux={'n_events': 450000} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wwz_amcatnlo',
    id=18150532,
    is_data=False,
    processes=[procs.wwz],
    keys=['/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM',
          '/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM'],
    n_files=2 + 16,
    n_events=1774030.0, # this n_events is the gensumwt
    aux={'n_events': 1950044} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wzz_amcatnlo',
    id=18150533,
    is_data=False,
    processes=[procs.wzz],
    keys=['/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM',
          '/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM'],
    n_files=1 + 16,
    n_events=1806418.0, # this n_events is the gensumwt
    aux={'n_events': 1987058} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='zzz_amcatnlo',
    id=18150534,
    is_data=False,
    processes=[procs.zzz],
    keys=['/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM',
          '/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM'],
    n_files=2 + 15,
    n_events=1751582.0, # this n_events is the gensumwt
    aux={'n_events': 1970234} # n_events in aux is the nEvents produced
)
