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

from CGRdb.models import load_tables
from pony.orm import Set, Json, buffer, left_join
from functools import reduce


class MoleculeSearch(object):
    @classmethod
    def structure_exists(cls, structure):
        structure_exists = cls.exist(fear = cls.get_fear(structure))
        if structure_exists:
            return MoleculeSearch.find_structure(cls,structure)
        return False

    @classmethod
    def find_structure(cls, structure):
        return cls.get(fear = cls.get_fear(structure))




class ReactionSearch(object):
    @classmethod
    def mapless_exists(cls, structure):
        fresh = cls.refresh_reaction(structure)
        if fresh:
            return cls.exists(mapless_fear=cls.get_mapless_fear(fresh))
        return False

    @classmethod
    def structure_exists(cls, structure):
        fresh = cls.refresh_reaction(structure)
        if fresh:
            return cls.exists(fear=cls.get_fear(fresh))
        return False

    @classmethod
    def find_reaction(cls,structure):
        return cls.get(fear=cls.get_fear(structure))

    @classmethod
    def find_reactions_by_molecule(cls,structure, product=None):
        if product is None:
            q = left_join(
                r for m in Molecules if m.fear == cls.get_fear(structure) for rs in m.reactions for r in
                rs.reactions)
        else:
            q = left_join(r for m in Molecules if m.fear == cls.get_fear(structure) for rs in m.reactions if
                          rs.product == product for r in rs.reactions)
        return list(q)

    @classmethod
    def find_reactions_by_molecules(cls,product=None, reagent=None):
        d = dict()
        if product is not None:
            for i in product:
                d[i] = set()
            for m, r in left_join(
                    (m.fear, r) for m in Molecules if m.fear in [cls.get_fear(x) for x in product] for rs in
                    m.reactions if rs.product for r in rs.reactions):
                d[m].add(r)

        if reagent is not None:
            for i in reagent:
                d[i] = set()
            for m, r in left_join(
                    (m.fear, r) for m in Molecules if m.fear in [cls.get_fear(x) for x in reagent] for rs in
                    m.reactions if not rs.product for r in rs.reactions):
                d[m].add(r)

        return reduce(set.intersection, d.values())