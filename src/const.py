"""Software wide constants""" 

SEED_MODE = 'seed'

NORMAL_MODE = 'normal'

NORMAL_SETTINGS_FILE = "NormalGameUserSettings.ini"

SEED_SETTINGS_FILE = "SeedGameUserSettings.ini"

GAME_SETTINGS_FILE = 'GameUserSettings.ini'

SETTINGS_DATA = """
;SEED_MODE
[D3DRHIPreference]
bUseD3D12InGame=False

[/Script/Squad.SQGameUserSettings]
PlayerNamePrefix="SEED"
MasterVolume=0.000000
EffectsVolume=0.000000
UIVolume=0.000000
MusicVolume=0.000000
UnfocusedVolumeMultiplier=0.250000
LastCPUBenchmarkResult=272.555908
LastGPUBenchmarkResult=598.617371
LastCPUBenchmarkSteps=269.873810
LastCPUBenchmarkSteps=274.343933
LastGPUBenchmarkSteps=834.823486
LastGPUBenchmarkSteps=569.236572
LastGPUBenchmarkSteps=1063.980225
LastGPUBenchmarkSteps=643.584045
LastGPUBenchmarkSteps=183.912811
LastGPUBenchmarkSteps=391.000519
LastGPUBenchmarkSteps=1388.207275
ResolutionSizeX=1024
ResolutionSizeY=768
LastUserConfirmedResolutionSizeX=1024
LastUserConfirmedResolutionSizeY=768
DesiredScreenWidth=1280
DesiredScreenHeight=720
GraphicsQuality=0
ScreenSharpening=(Value=0)
LensFlareQuality=(Value=0)
ScreenPercentage=(Value=50)
MaxAnisotropy=(Value=4)
ScopeUpdateRate=(Value=30)
ScopeResolutionScale=(Value=1112014848)
FSR2Quality=(Value=2)
FSR2Sharpness=(Value=1060320051)
MaterialQuality=(Value=0)
CrouchMode=Toggle
ADSMode=Toggle
LeanMode=Toggle
FreelookMode=Hold
SprintMode=Hold
SquadIncrementalVersion=1
bClientAutoRecord=False
NumberAutoRecordedGames=5
bIsAAEnabled=True
LastSavedScopeClarityMode=0
bIsPlayerADSWithScopeClarityOn=False
LastSavedAASamples=4
ControlsPresetName=INVTEXT("Default")
HZBOcclusion=(Value=0)
TextureStreamPoolSizeStorage=(Value=0)
bCompassBackgroundEnabled=False
bCompassTopViewEnabled=False
GlobalSensitivity=1.000000
Tessellation=(Value=0)
TessellationMode=(Value=4294967295)
bHelicopterInvertMousePitch=False
HelicopterPitchSensitivity=1.000000
bUncapTexturePoolSize=False
HelicopterRollSensitivity=1.000000
SoldierSensitivity=1.000000
SoldierZoomSensitivities=((1.000000, 1.000000),(2.000000, 0.500000),(3.000000, 0.330000),(4.000000, 0.250000),(6.000000, 0.170000),(8.000000, 0.130000),(12.000000, 0.080000))
VehicleSensitivity=1.000000
PostFX_Brightness=1.000000
PostFX_Contrast=1.000000
PostFX_Saturation=1.000000
ContactShadows=(Value=1)
FoliageMinLOD=(Value=0)
VehicleZoomSensitivities=((1.000000, 1.000000),(4.000000, 0.500000))
bFreelookRecentersWeapon=False
MenuFrameRateLimit=10.000000
BrowserSearchTags=mode_invasion
BrowserSearchTags=mode_aas
BrowserSearchTags=mode_raas
BrowserSearchTags=mode_destruction
BrowserSearchTags=mode_tc
BrowserSearchTags=mode_insurgency
BrowserSearchTags=mode_seed
BrowserSearchTags=mode_skirmish
BrowserSearchTags=mode_training
QPPreferedLanguage=en
QPGameModes=AAS
QPGameModes=RAAS
QPGameModes=Insurgency
QPGameModes=Invasion
QPGameModes=Seed
QPGameModes=Territory Control
QPGameModes=Skirmish
QPGameModes=Training
QPSearchTags=language_en
AmbientOcclusion=(Value=0)
AntiAliasingMode=(Value=0)
ScopeClarityMode=(Value=1)
GPUThresholdScores=175
GPUThresholdScores=250
GPUThresholdScores=350
CPUThresholdScores=110
CPUThresholdScores=130
CPUThresholdScores=175
OceanQuality=(Value=0)
WakeSim=(Value=0)
SkeletalMeshLODBias=(Value=0)
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Emote_Hello.Emote_Hello
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_PointForward.Gesture_PointForward
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_MoveOut.Gesture_MoveOut
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_ComeHere.Gesture_ComeHere
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Emote_Shrug.Emote_Shrug
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/EmoteSalute.EmoteSalute
EquippedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_ThumbsUp.Gesture_ThumbsUp
ViewedBundles=/Game/Bazaar/Free_Pack.Free_Pack
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Emote_Hello.Emote_Hello
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_PointForward.Gesture_PointForward
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_MoveOut.Gesture_MoveOut
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/EmoteSalute.EmoteSalute
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_ThumbsUp.Gesture_ThumbsUp
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Gesture_ComeHere.Gesture_ComeHere
ViewedEmotes=/Game/Art/Soldier_Animations/BazaarEmotes/EmoteData/Emote_Shrug.Emote_Shrug
SquadVoiceVolume=1.700000
bApplyBiasWhileNonLeader=False
JoyStickConfigurations=((Pitch, ()),(Roll, ()),(Yaw, ()),(Collective, ()))
bAlwaysFreeLook=False
StreamerModeMask=0
SquadSettingsVersion=10
bUseDynamicResolution=False
LastConfirmedAudioQualityLevel=3
FrameRateLimit=20.000000
LastUserConfirmedDesiredScreenWidth=1280
LastUserConfirmedDesiredScreenHeight=720
bUseHDRDisplayOutput=False
HDRDisplayOutputNits=1000

[ScalabilityGroups]
sg.ResolutionQuality=0.000000
sg.ViewDistanceQuality=0
sg.AntiAliasingQuality=0
sg.ShadowQuality=0
sg.PostProcessQuality=0
sg.TextureQuality=0
sg.EffectsQuality=0
sg.FoliageQuality=0
sg.ShadingQuality=0

[/Script/Engine.GameUserSettings]
bUseDesiredScreenHeight=False
"""