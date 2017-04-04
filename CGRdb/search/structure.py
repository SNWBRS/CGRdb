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

class MoleculeSearch(object):
    @classmethod
    def structure_exists(cls, structure):
        structure_exists = cls.get_fear(structure)
        if structure_exists:
            return MoleculeSearch.find_structure(cls,structure)
        return False


    @classmethod
    def find_structure(cls, structure):
        return cls.get_fear(structure)




class ReactionSearch(object):
    @classmethod
    def mapless_exists(cls, structure): #структура самой реакции
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
    def find_structure(cls, structure):
        return
        pass

