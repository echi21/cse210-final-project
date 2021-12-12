import pathlib


class FogLib:

    def __init__(self):
        self.fog_library = []
        self.set_path()

    def set_path(self):

        self.fog_library = [
            (pathlib.Path(__file__).parent / "images/fog/frame_00_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_01_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_02_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_03_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_04_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_05_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_06_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_07_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_08_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_09_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_10_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_11_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_12_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_13_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_14_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_15_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_16_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_17_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_18_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_19_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_20_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_21_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_22_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_23_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_24_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_25_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_26_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_27_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_28_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_29_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_30_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_31_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_32_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_33_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_34_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_35_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_36_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_37_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_38_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_39_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_40_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_41_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_42_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_43_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_44_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_45_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_46_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_47_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_48_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_49_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_50_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_51_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_52_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_53_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_54_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_55_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_56_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_57_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_58_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_59_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_60_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_61_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_62_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_63_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_64_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_65_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_66_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_67_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_68_delay-0.08s.png"),
            (pathlib.Path(__file__).parent / "images/fog/frame_69_delay-0.08s.png")
        ]

    def get_fog_list(self):
        return self.fog_library
