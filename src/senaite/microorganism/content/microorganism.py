# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.MICROORGANISM.
#
# SENAITE.MICROORGANISM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2020 by it's authors.
# Some rights reserved, see README and LICENSE.

from bika.lims.catalog import SETUP_CATALOG

from plone.dexterity.content import Container
from plone.supermodel import model

from senaite.microorganism import messageFactory as _
from zope import schema
from zope.interface import implementer


class IMicroorganism(model.Schema):
    """Microorganism content interface
    """
    gram_stain = schema.Choice(
        title=_(u"Gram stain"),
        description=_(
            ""
        ),
        vocabulary="senaite.microorganism.vocabularies.gram_stains",
        default="Undefined",
    )

    glass = schema.Bool(
        title=_(u"GLASS organism"),
        description=_(
            "Whether this is an infectious organism included in the Global "
            "Antimicrobial Resistance Surveillance System (GLASS) for the "
            "the collection, analysis and sharing of Antimicrobial Resistance "
            "(AMR) data at a global level"
        ),
        required=False,
    )

    multi_resistant = schema.Bool(
        title=_(u"MRO Organism"),
        description=_(
            "Whether this organism is considered multi resistant (MRO)",
        ),
        required=False,
    )

    mro_phenotype = schema.TextLine(
        title=_(u"MRO phenotype"),
        required=False,
    )


@implementer(IMicroorganism)
class Microorganism(Container):
    """Microorganism content
    """
    # Catalogs where this type will be catalogued
    _catalogs = [SETUP_CATALOG]