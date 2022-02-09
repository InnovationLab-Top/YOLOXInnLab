#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 1.0
        self.width = 1.0
        self.scale = (0.5, 1.5)
        self.random_size = (30, 50)
        self.test_size = (1280, 1280)
        self.input_size = (1280, 1280)
        self.num_classes = 1
        abs_path = os.path.realpath(__file__)
        self.output_dir = "/valohai/outputs"
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

