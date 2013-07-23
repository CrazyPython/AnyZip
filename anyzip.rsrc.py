{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'AnyZip',
          'size':(1616, 876),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'List', 
    'name':'filenamesdis', 
    'position':(3, 161), 
    'items':[], 
    },

{'type':'Button', 
    'name':'zip', 
    'position':(233, 25), 
    'label':u'zippify', 
    },

{'type':'StaticText', 
    'name':'load', 
    'position':(353, 228), 
    'size':(30, -1), 
    'visible':False, 
    },

{'type':'Button', 
    'name':'run', 
    'position':(310, 25), 
    'label':u'run', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(23, 94), 
    'text':u'Open...', 
    },

{'type':'Button', 
    'name':'browse2', 
    'position':(205, 116), 
    'label':u'Browse...', 
    },

{'type':'TextField', 
    'name':'secondary', 
    'position':(71, 117), 
    'size':(127, -1), 
    'toolTip':u'combine/compress from/depress to/run with args', 
    },

{'type':'Button', 
    'name':'browse', 
    'position':(204, 90), 
    'label':u'Browse...', 
    },

{'type':'TextField', 
    'name':'url', 
    'position':(70, 91), 
    'size':(127, -1), 
    'toolTip':u'View, edit, delete, extract this', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(350, 225), 
    'size':(1, 20), 
    'layout':'horizontal', 
    },

{'type':'Button', 
    'name':'combine', 
    'position':(310, 0), 
    'label':u'combine', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(1, 225), 
    'size':(390, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'msg', 
    'position':(1, 228), 
    'text':u'Ready', 
    },

{'type':'Button', 
    'name':'delete', 
    'position':(235, 0), 
    'label':u'delete', 
    },

{'type':'Button', 
    'name':'extract', 
    'position':(160, 0), 
    'label':u'extract', 
    },

{'type':'Button', 
    'name':'edit', 
    'position':(80, 0), 
    'label':u'edit', 
    },

{'type':'Button', 
    'name':'view', 
    'position':(1, 0), 
    'label':u'view', 
    },

] # end components
} # end background
] # end backgrounds
} }
