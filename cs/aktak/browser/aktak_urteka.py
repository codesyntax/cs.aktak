
__version__ = '$Id$'

from Products.CMFPlone import utils

import DateTime
import pdb
from Acquisition import aq_inner, aq_parent
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
import random
class Aktak(BrowserView):

	def __call__(self):
                #import pdb;pdb.set_trace()
                
		context=aq_inner(self.context)
                urteak=aq_parent(context).getFolderContents({'portal_type':'DonEdukia'})
                dict={}
                for urtea in urteak:
                    dict[urtea.Title]={}
                    barrukoak=urtea.getObject().getFolderContents({'portal_type':'DonEdukia'})
                    for i in barrukoak:
                            
                        aktak=i.getObject().getFolderContents({'portal_type':'File','sort_on':'created','sort_order':'reverse'}, full_objects=1)
                        dict[urtea.Title][i.Title]=aktak
                return dict
