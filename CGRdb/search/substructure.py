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
from CGRtools.CGRreactor import CGRreactor


class MoleculeSearch(object):
    @classmethod
    def find_substructures(cls, structure):
        res = []
        cgrr = CGRreactor()
        for se in cls.find_similar(structure):
            gm = cgrr.get_cgr_matcher(se.structure_raw, structure)
            if gm.subgraph_is_isomorphic():
                res.append(se)

        return res


class ReactionSearch(object):
    @classmethod
    def find_substructures(cls, structures):
        pass
