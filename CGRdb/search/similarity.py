# -*- coding: utf-8 -*-
#
#  Copyright 2017 Ramil Nugmanov <stsouko@live.ru>
#  This file is part of CGRdb.
#
#  CGRdb is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import numpy as np
import pickle
from sklearn.neighbors import BallTree
from pony.orm import select
from os import path

dump_dir = ':C'

class Similarity(object):
    @classmethod
    def load_tree(cls, reindex=False):
        cls_path = path.join(dump_dir, '%s.bin' % cls.__name__)

        if reindex or cls.__name__ not in cls.__cached_tree:
            a = []
            ids = []
            for fp, i in select((s.fingerprint, s.id) for s in cls):
                by_x = np.unpackbits(np.fromstring(fp, dtype=np.uint8))
                a.append(by_x)
                ids.append(i)

            tree = BallTree(np.matrix(a), metric='jaccard')
            with open(cls_path, 'wb') as f:
                pickle.dump((tree, ids), f)

            cls.__cached_tree[cls.__name__] = (tree, ids)

        else:
            with open(cls_path, 'rb') as f:
                cls.__cached_tree[cls.__name__] = pickle.load(f)

    __cached_tree = {}

    @classmethod
    def find_similar(cls, structures):

        pass
