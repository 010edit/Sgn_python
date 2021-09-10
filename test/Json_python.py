import json

INSTRUCTIONS  = '''
[
  {
    "Mnemonic": "AAD",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "AAM",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ADC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ADCX",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ADD",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ADOX",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "AND",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BLSI",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BLSMSK",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BLSR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BSF",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BSR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BSWAP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "imm8",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BTC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "imm8",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BTR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "imm8",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "BTS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "imm8",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CALL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CLFLUSH",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CLFLUSHOPT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CLWB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVA",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVAE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVBE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVG",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVGE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVLE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNA",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNAE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNBE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNG",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNGE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNLE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNO",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVNZ",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVO",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMOVPE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CMPS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      },
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "CRC32",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r32",
          "r32",
          "r32",
          "r32",
          "r64",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m8",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "DEC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r16",
          "r32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "DIV",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ENTER",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "imm16"
        ]
      },
      {
        "Types": [
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "FSTSW",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AX"
        ]
      }
    ]
  },
  {
    "Mnemonic": "FNSTSW",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AX"
        ]
      }
    ]
  },
  {
    "Mnemonic": "IDIV",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "IMUL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "INC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r16",
          "r32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "INS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8",
          "m16",
          "m32"
        ]
      },
      {
        "Types": [
          "DX",
          "DX",
          "DX"
        ]
      }
    ]
  },
  {
    "Mnemonic": "INVLPG",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m"
        ]
      }
    ]
  },
  {
    "Mnemonic": "JMP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "LDMXCSR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "VLDMXCSR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "LEA",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "m",
          "m",
          "m"
        ]
      }
    ]
  },
  {
    "Mnemonic": "LMSW",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "LODS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "LZCNT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MOV",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm64",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MOVBE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "m16",
          "m32",
          "m64"
        ]
      },
      {
        "Types": [
          "m16",
          "m32",
          "m64",
          "r16",
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MOVNTI",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m32",
          "m64"
        ]
      },
      {
        "Types": [
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MOVS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      },
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MOVSX",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MOVZX",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "MUL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "NEG",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "NOP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "NOT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "OR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "OUT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "imm8",
          "imm8",
          "imm8",
          "DX",
          "DX",
          "DX"
        ]
      },
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "AL",
          "AX",
          "EAX"
        ]
      }
    ]
  },
  {
    "Mnemonic": "OUTS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "DX",
          "DX",
          "DX"
        ]
      },
      {
        "Types": [
          "m8",
          "m16",
          "m32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "POP",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64",
          "r16",
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "POPCNT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PREFETCHT0",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PREFETCHT1",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PREFETCHT2",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PREFETCHNTA",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PREFETCHW",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PREFETCHWT1",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "PUSH",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64",
          "r16",
          "r32",
          "r64",
          "imm8",
          "imm16",
          "imm32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "RCL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "RCR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ROL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "ROR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "RDRAND",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "RDSEED",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "RET",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "imm16",
          "imm16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SAL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SAR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SHL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SHR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "CL",
          "CL",
          "imm8",
          "imm8",
          "CL",
          "imm8",
          "CL",
          "CL",
          "imm8",
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SBB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SCAS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETA",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETAE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETBE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETG",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETGE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETLE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNA",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNAE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNBE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNC",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNG",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNGE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNL",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SETNLE",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SGDT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SIDT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SLDT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SMSW",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "STMXCSR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "VSTMXCSR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m32"
        ]
      }
    ]
  },
  {
    "Mnemonic": "STOS",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8",
          "m16",
          "m32",
          "m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "STR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "SUB",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "TEST",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "TZCNT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "VERR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "VERW",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m16"
        ]
      }
    ]
  },
  {
    "Mnemonic": "XABORT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "imm8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "XADD",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      },
      {
        "Types": [
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      }
    ]
  },
  {
    "Mnemonic": "XLAT",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "m8"
        ]
      }
    ]
  },
  {
    "Mnemonic": "XOR",
    "V64": true,
    "V32": true,
    "Operands": [
      {
        "Types": [
          "AL",
          "AX",
          "EAX",
          "RAX",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m16",
          "r/m32",
          "r/m64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64"
        ]
      },
      {
        "Types": [
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm16",
          "imm32",
          "imm32",
          "imm8",
          "imm8",
          "imm8",
          "r8",
          "r8",
          "r16",
          "r32",
          "r64",
          "r/m8",
          "r/m8",
          "r/m16",
          "r/m32",
          "r/m64"
        ]
      }
    ]
  }
]
'''

js = json.loads(INSTRUCTIONS)
print(js)
