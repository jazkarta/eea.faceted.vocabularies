""" Widget positions vocabularies
"""
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from eea.faceted.vocabularies.utils import IVocabularyFactory
from eea.faceted.vocabularies import EEAMessageFactory as _


@implementer(IVocabularyFactory)
class WidgetPositions(object):
    """ Widget position in page
    """

    def __call__(self, *args, **kwargs):

        positions = (
            SimpleTerm('top', 'top', _('Top')),
            SimpleTerm('left', 'left', _('Left')),
            SimpleTerm('center', 'center', _('Center top')),
            SimpleTerm('right', 'right', _('Right')),
            SimpleTerm('bottomcenter', 'bottomcenter', _('Center bottom')),
            SimpleTerm('bottom', 'bottom', _('Bottom')),
        )
        return SimpleVocabulary(positions)
