from iced_x86 import Decoder, Formatter, FormatterSyntax

data = b''

with open('nopeeking', 'rb') as f:
    data = f.read()

formatter = Formatter(FormatterSyntax.MASM)
formatter.branch_leading_zeros = False
formatter.space_after_operand_separator = True

# These addresses are the entry points to the `ud2`-heavy flows
for rip in (0x1047, 0x127A):
    cont = True

    while cont:
        decoder = Decoder(64, data[rip:], ip=rip)

        for instr in decoder:
            finstr = formatter.format(instr)
            print(f'{instr.ip:04X}h {finstr}')

            if finstr == 'ud2':
                tag = data[instr.next_ip] + (data[instr.next_ip+1] << 8)
                rip = instr.ip + 4

                print('---')
                print(f'TAG: 0x{tag:02X}')
                print('---')
                break

            if finstr == 'ret':
                cont = False
                break

    print('='*80)
