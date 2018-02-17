
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

class FillVestingWithdrawOperation(Base, BaseOperation):
    """
    
    
    Steem Blockchain Example
    ======================

    

    """
    
    __tablename__ = 'sbds_op_fill_vesting_withdraws'
    __operation_type__ = 'fill_vesting_withdraw_operation'
    
    from_account = Column(String(50), index=True) # steem_type:account_name_type
    to_account = Column(String(50), index=True) # steem_type:account_name_type
    withdrawn = Column(Numeric(15,6), nullable=False) # steem_type:asset
    withdrawn_symbol = Column(String(5)) # steem_type:asset
    deposited = Column(Numeric(15,6), nullable=False) # steem_type:asset
    deposited_symbol = Column(String(5)) # steem_type:asset
    operation_type = Column(
        operation_types_enum,
        nullable=False,
        index=True,
        default='fill_vesting_withdraw_operation')
    
    _fields = dict(
        from_account=lambda x: x.get('from_account'),
        to_account=lambda x: x.get('to_account'),
        withdrawn=lambda x: amount_field(x.get('withdrawn'), num_func=float),
        withdrawn_symbol=lambda x: amount_symbol_field(x.get('withdrawn')),
        deposited=lambda x: amount_field(x.get('deposited'), num_func=float),
        deposited_symbol=lambda x: amount_symbol_field(x.get('deposited')),
    )

