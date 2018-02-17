
# coding=utf-8
import os.path

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import Boolean
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import BigInteger

from sqlalchemy.dialects.mysql import JSON

from toolz import get_in

from ... import Base
from ....enums import operation_types_enum
from ....field_handlers import amount_field
from ....field_handlers import amount_symbol_field
from ....field_handlers import comment_body_field
from ..base import BaseOperation

class TransferToVestingOperation(Base, BaseOperation):
    """
    
    
    Steem Blockchain Example
    ======================
    {
      "amount": "357.000 STEEM",
      "from": "faddy",
      "to": ""
    }
    

    """
    
    __tablename__ = 'sbds_op_transfer_to_vestings'
    __operation_type__ = 'transfer_to_vesting_operation'
    
    _from = Column('from', Unicode(50), index=True) # name:from
    to = Column(String(50), index=True) # steem_type:account_name_type
    amount = Column(Numeric(15,6), nullable=False) # steem_type:asset
    amount_symbol = Column(String(5)) # steem_type:asset
    operation_type = Column(
        operation_types_enum,
        nullable=False,
        index=True,
        default='transfer_to_vesting_operation')
    
    _fields = dict(
        _from=lambda x: x.get('from'),
        to=lambda x: x.get('to'),
        amount=lambda x: amount_field(x.get('amount'), num_func=float),
        amount_symbol=lambda x: amount_symbol_field(x.get('amount')),
    )

