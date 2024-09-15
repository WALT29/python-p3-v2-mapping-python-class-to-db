#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department
import ipdb

Department.drop_table()
Department.create_table()

# payroll=Department("Payroll","Building A 5th Floor")
# print(payroll)
# payroll.save()
# print(payroll)

# hr=Department("Human Resource","Building A 8th Floor")
# print(hr)
# hr.save()
# print(hr)

payroll=Department.create("Payroll","Building A 5th Floor")
print(payroll)

hr=Department.create("Human Resource","Building A 8th Floor")
print(hr)

payroll.name="PAYROLL DEPARTMENT"
payroll.location="NAIROBI CENTRAL"
payroll.update();

hr.delete()



ipdb.set_trace()
