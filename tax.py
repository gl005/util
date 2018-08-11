#!/usr/bin/env python3

import sys
import argparse


def calc_amount_net(amount):
    return amount / 1.21


# Estimates the effective cost, given a price of something and the tax deduction percentage
def calc_deduct(amount, percentage_deductable):
    amount_net = calc_amount_net(amount)
    vat = amount - amount_net
    deductable_factor = percentage_deductable / 100
    fiscal_vat = vat * deductable_factor
    fiscal_amount = amount_net * deductable_factor
    tax_return = fiscal_amount * 0.5  # assumes the cost influences the earnings in the highest bracket
    real_price = amount - fiscal_vat - tax_return

    print('VAT:\t\t%f' % vat)
    print('Net:\t\t%f' % amount_net)
    print('=======================================')
    print('VAT returns:\t%f' % fiscal_vat)
    print('Tax returns:\t%f' % tax_return)
    print('Real price:\t%f' % real_price)


# Estimates how much of an invoices needs to be saved for future costs & taxes
def calc_savings(amount):
    amount_net = calc_amount_net(amount)
    tax = amount - amount_net
    to_save = (amount_net / 2) + tax
    to_keep = amount_net / 2

    print('Save:\t\t%f' % to_save)
    print('Remainder:\t%f' % to_keep)
    print('=======================================')
    print('Net amount:\t%f' % amount_net)
    print('Tax:\t\t%f' % tax)
    print('Total amount:\t%f' % amount)


parser = argparse.ArgumentParser(description='Use --deduct to estimate price after tax deductions', usage='taxes <amount> [<args>]')
parser.add_argument('amount', help='full amount')
parser.add_argument('--deduct', type=float, help='use this parameter to calculate deductibility')
amount = float(parser.parse_args(sys.argv[1:2]).amount)
args = parser.parse_args()
deduct = args.deduct

if deduct is not None:
    calc_deduct(amount, deduct)
else:
    calc_savings(amount)
