
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCEPT CLOSE_CLIENT CLOSE_SERVER OPEN_CLIENT OPEN_SERVER SEND\n    statement : open_client\n            | open_server\n            | send\n            | close_client\n            | accept\n            | close_server\n    open_client : OPEN_CLIENTopen_server : OPEN_SERVERsend : SENDclose_client : CLOSE_CLIENTaccept : ACCEPTclose_server : CLOSE_SERVER'
    
_lr_action_items = {'OPEN_CLIENT':([0,],[8,]),'OPEN_SERVER':([0,],[9,]),'SEND':([0,],[10,]),'CLOSE_CLIENT':([0,],[11,]),'ACCEPT':([0,],[12,]),'CLOSE_SERVER':([0,],[13,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'open_client':([0,],[2,]),'open_server':([0,],[3,]),'send':([0,],[4,]),'close_client':([0,],[5,]),'accept':([0,],[6,]),'close_server':([0,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> open_client','statement',1,'p_statement','parser.py',19),
  ('statement -> open_server','statement',1,'p_statement','parser.py',20),
  ('statement -> send','statement',1,'p_statement','parser.py',21),
  ('statement -> close_client','statement',1,'p_statement','parser.py',22),
  ('statement -> accept','statement',1,'p_statement','parser.py',23),
  ('statement -> close_server','statement',1,'p_statement','parser.py',24),
  ('open_client -> OPEN_CLIENT','open_client',1,'p_open_client','parser.py',36),
  ('open_server -> OPEN_SERVER','open_server',1,'p_open_server','parser.py',41),
  ('send -> SEND','send',1,'p_send','parser.py',49),
  ('close_client -> CLOSE_CLIENT','close_client',1,'p_client_close','parser.py',55),
  ('accept -> ACCEPT','accept',1,'p_accept','parser.py',60),
  ('close_server -> CLOSE_SERVER','close_server',1,'p_server_close','parser.py',65),
]