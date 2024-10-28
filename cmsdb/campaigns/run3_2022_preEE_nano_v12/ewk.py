# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################

# inclusive, LO, forPog
cpn.add_dataset(
    name="dy_m50toinf_for_pog_madgraph",
    id=14802794,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv12-forPOG_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=27096229,
)

#
# NLO
#
cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14950158,
    processes=[procs.dy_m4to10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=624,
            n_events=99285491,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14803891,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=141,
            n_events=67681922,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
            ],
            n_files=73,
            n_events=47494002,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14796042,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=115,
            n_events=65997137,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
            ],
            n_files=259,
            n_events=97500666,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14791297,
    processes=[procs.dy_m50toinf_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=173,
            n_events=105230672,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14791387,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=196,
            n_events=99076102,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14790870,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=177,
            n_events=75705368,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14826040,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=215,
            n_events=47125505,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14825639,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=168,
            n_events=18503737,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14826712,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=1939721,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14823834,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=503786,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14831319,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=508646,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14826102,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=81,
            n_events=18752305,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14826076,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=174,
            n_events=18592664,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14825454,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=3549847,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14824816,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=488707,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14826080,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=474576,
        ),
    ),
)



cpn.add_dataset(
    name="z_qq_pt400to600_2j_amcatnlo",
    id=14825757,
    processes=[procs.z_qq_pt400to600_2j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=710337,
)

cpn.add_dataset(
    name="z_qq_pt600toinf_1j_amcatnlo",
    id=14831039,
    processes=[procs.z_qq_pt600toinf_1j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=519778,
)

cpn.add_dataset(
    name="z_qq_pt100to200_1j_amcatnlo",
    id=14823826,
    processes=[procs.z_qq_pt100to200_1j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=10001668,
)

cpn.add_dataset(
    name="z_qq_pt100to200_2j_amcatnlo",
    id=14821758,
    processes=[procs.z_qq_pt100to200_2j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=95,
    n_events=8995099,
)

cpn.add_dataset(
    name="z_qq_pt200to400_1j_amcatnlo",
    id=14822098,
    processes=[procs.z_qq_pt200to400_1j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=4399261,
)

cpn.add_dataset(
    name="z_qq_pt200to400_2j_amcatnlo",
    id=14818881,
    processes=[procs.z_qq_pt200to400_2j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=70,
    n_events=9778689,
)

cpn.add_dataset(
    name="z_qq_pt400to600_1j_amcatnlo",
    id=14820240,
    processes=[procs.z_qq_pt400to600_1j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=481551,
)

cpn.add_dataset(
    name="z_qq_pt600toinf_2j_amcatnlo",
    id=14833138,
    processes=[procs.z_qq_pt600toinf_2j],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=540869,
)

cpn.add_dataset(
    name="z_tautau_3mu_m60to120_pythia",
    id=14790625,
    processes=[procs.z_tautau_3mu_m60to120],
    keys=[
        "/Zto2Tauto3Mu_M-60to120_TuneCP5_13p6TeV_pythia8-evtgen/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=195001,
)

cpn.add_dataset(
    name="z_tautau_6mu_m60to120_pythia",
    id=14805323,
    processes=[procs.z_tautau_6mu_m60to120],
    keys=[
        "/Zto2Tauto6Mu_M-60to120_TuneCP5_13p6TeV_pythia8-evtgen/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=201131,
)

####################################################################################################
#
# W boson production
#
####################################################################################################

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14803995,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=148,
    n_events=84739011,
)

#
# Diboson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14800098,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=15357390,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14803901,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7527043,
)

cpn.add_dataset(
    name="zz_pythia",
    id=14808010,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=1181750,
)

####################################################################################################
# Triboson
####################################################################################################

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14800679,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=450000,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14797985,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=1950044,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14796198,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=1987058,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14801345,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=1970234,
)