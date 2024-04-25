WIDTH = 16
HEIGHT = 16
flag = 'gb16'
FIRST = 0x20
LAST = 0x7f
FONT = {
    'HEIGHT':
    16,
    'WIDTH':
    16,
    'SIZE':
    32,
    '当': [
        0x01, 0x00, 0x21, 0x08, 0x11, 0x08, 0x09, 0x10, 0x09, 0x20, 0x01, 0x00,
        0x7f, 0xf8, 0x00, 0x08, 0x00, 0x08, 0x00, 0x08, 0x3f, 0xf8, 0x00, 0x08,
        0x00, 0x08, 0x00, 0x08, 0x7f, 0xf8, 0x00, 0x08
    ],
    '前': [
        0x10, 0x10, 0x08, 0x10, 0x08, 0x20, 0xff, 0xfe, 0x00, 0x00, 0x3e, 0x08,
        0x22, 0x48, 0x22, 0x48, 0x3e, 0x48, 0x22, 0x48, 0x22, 0x48, 0x3e, 0x48,
        0x22, 0x08, 0x22, 0x08, 0x2a, 0x28, 0x24, 0x10
    ],
    '天': [
        0x00, 0x00, 0x3f, 0xf8, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00,
        0xff, 0xfe, 0x01, 0x00, 0x02, 0x80, 0x02, 0x80, 0x04, 0x40, 0x04, 0x40,
        0x08, 0x20, 0x10, 0x10, 0x20, 0x08, 0xc0, 0x06
    ],
    '气': [
        0x10, 0x00, 0x10, 0x00, 0x3f, 0xfc, 0x20, 0x00, 0x4f, 0xf0, 0x80, 0x00,
        0x3f, 0xf0, 0x00, 0x10, 0x00, 0x10, 0x00, 0x10, 0x00, 0x10, 0x00, 0x10,
        0x00, 0x0a, 0x00, 0x0a, 0x00, 0x06, 0x00, 0x02
    ],
    '美': [
        0x08, 0x20, 0x04, 0x40, 0x7f, 0xfc, 0x01, 0x00, 0x01, 0x00, 0x3f, 0xf8,
        0x01, 0x00, 0x01, 0x00, 0xff, 0xfe, 0x01, 0x00, 0x01, 0x00, 0x7f, 0xfc,
        0x02, 0x80, 0x04, 0x40, 0x18, 0x30, 0xe0, 0x0e
    ],
    '丽': [
        0x00, 0x00, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x3e, 0xf8, 0x22, 0x88,
        0x22, 0x88, 0x22, 0x88, 0x32, 0xc8, 0x2a, 0xa8, 0x2a, 0xa8, 0x22, 0x88,
        0x22, 0x88, 0x22, 0x88, 0x2a, 0xa8, 0x24, 0x90
    ],
    '浙': [
        0x02, 0x08, 0x42, 0x1c, 0x22, 0x60, 0x22, 0x40, 0x0f, 0xc0, 0x82, 0x40,
        0x42, 0x7e, 0x52, 0xc8, 0x13, 0x48, 0x2e, 0x48, 0xe2, 0x48, 0x22, 0x48,
        0x22, 0x48, 0x22, 0x48, 0x2a, 0x88, 0x05, 0x08
    ],
    '江': [
        0x00, 0x00, 0x20, 0x00, 0x17, 0xfc, 0x10, 0x40, 0x80, 0x40, 0x40, 0x40,
        0x48, 0x40, 0x08, 0x40, 0x10, 0x40, 0x10, 0x40, 0xe0, 0x40, 0x20, 0x40,
        0x20, 0x40, 0x2f, 0xfe, 0x20, 0x00, 0x00, 0x00
    ],
    '章': [0x02,0x00,0x01,0x00,0x3f,0xf8,0x08,0x20,0x04,0x40,0xff,0xfe,0x00,0x00,0x1f,0xf0,0x10,0x10,0x1f,0xf0,0x10,0x10,0x1f,0xf0,0x01,0x00,0xff,0xfe,0x01,0x00,0x01,0x00],
    
    '永': [0x02,0x00,0x01,0x00,0x00,0x80,0x1f,0x00,0x01,0x04,0x01,0x08,0x7d,0x90,0x05,0xa0,0x05,0x40,0x09,0x40,0x09,0x20,0x11,0x10,0x21,0x08,0xc1,0x06,0x05,0x00,0x02,0x00],

    '琪': [0x01,0x08,0x01,0x08,0xfb,0xfc,0x21,0x08,0x21,0x08,0x21,0xf8,0x21,0x08,0xf9,0x08,0x21,0xf8,0x21,0x08,0x21,0x08,0x3b,0xfe,0xe0,0x00,0x40,0x90,0x01,0x08,0x02,0x04],

    '最': [0x1f,0xf0,0x10,0x10,0x1f,0xf0,0x10,0x10,0x1f,0xf0,0x00,0x00,0xff,0xfe,0x22,0x00,0x3e,0xf8,0x22,0x88,0x3e,0x90,0x22,0x50,0x2f,0x20,0xf2,0x50,0x42,0x88,0x03,0x06],

    '帅': [0x08,0x20,0x08,0x20,0x48,0x20,0x48,0x20,0x49,0xfc,0x49,0x24,0x49,0x24,0x49,0x24,0x49,0x24,0x49,0x24,0x49,0x24,0x09,0x34,0x11,0x28,0x10,0x20,0x20,0x20,0x40,0x20],
};


FONT_32 = {
    'WIDTH':
    32,
    'HEIGHT':
    32,
    'SIZE':
    128,
    '℃': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x0f, 0x80, 0x00, 0x00, 0x1f, 0xc3, 0xff, 0x00,
        0x1d, 0xc7, 0xff, 0xb0, 0x1d, 0xcf, 0x83, 0xf0, 0x1d, 0xde, 0x00, 0xf0,
        0x1f, 0xfc, 0x00, 0x70, 0x07, 0x3c, 0x00, 0x70, 0x00, 0x78, 0x00, 0x30,
        0x00, 0x78, 0x00, 0x30, 0x00, 0x78, 0x00, 0x30, 0x00, 0x78, 0x00, 0x00,
        0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00,
        0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x30, 0x00, 0x3e, 0x00, 0x70,
        0x00, 0x1f, 0x01, 0xe0, 0x00, 0x0f, 0x87, 0xc0, 0x00, 0x07, 0xff, 0x80,
        0x00, 0x03, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '当': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xc0, 0x00,
        0x00, 0x03, 0xe0, 0x00, 0x0e, 0x03, 0xc1, 0xc0, 0x0f, 0x83, 0xc3, 0xe0,
        0x07, 0xc3, 0xc3, 0xe0, 0x03, 0xe3, 0xc7, 0xc0, 0x01, 0xf3, 0xcf, 0x00,
        0x00, 0xf3, 0xce, 0x00, 0x00, 0xf3, 0xdc, 0x00, 0x00, 0x03, 0xf8, 0x00,
        0x00, 0x03, 0xc0, 0x78, 0x1f, 0xff, 0xff, 0xfc, 0x0e, 0x00, 0x00, 0x78,
        0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78,
        0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x07, 0xff, 0xff, 0xf8,
        0x03, 0x80, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78,
        0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78,
        0x00, 0x00, 0x00, 0x78, 0x1f, 0xff, 0xff, 0xf8, 0x1e, 0x00, 0x00, 0x78,
        0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x00
    ],
    '前': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x0e, 0x00,
        0x00, 0x78, 0x0f, 0x00, 0x00, 0x7c, 0x1f, 0x00, 0x00, 0x3c, 0x1c, 0x00,
        0x00, 0x3c, 0x38, 0x38, 0x00, 0x1c, 0x70, 0x7c, 0x7f, 0xff, 0xff, 0xfe,
        0x38, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0xe0, 0x0e, 0x0f, 0x00, 0xf0,
        0x0f, 0xff, 0x3c, 0xe0, 0x0f, 0x0e, 0x3c, 0xe0, 0x0f, 0x0e, 0x38, 0xe0,
        0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0xfe, 0x38, 0xe0,
        0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0,
        0x0f, 0xfe, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0,
        0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x3c, 0xe0, 0x0f, 0x0e, 0x30, 0xe0,
        0x0f, 0x0e, 0x3d, 0xe0, 0x0f, 0x7e, 0x3f, 0xe0, 0x0f, 0x3e, 0x07, 0xc0,
        0x0f, 0x1c, 0x03, 0xc0, 0x00, 0x00, 0x00, 0x00
    ],
    '天': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0x03, 0xe0, 0x0f, 0xff, 0xff, 0xf0,
        0x07, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00,
        0x00, 0x03, 0x80, 0x00, 0x00, 0x07, 0x80, 0x00, 0x00, 0x07, 0x80, 0x00,
        0x00, 0x07, 0x80, 0x70, 0x00, 0x07, 0x80, 0xf8, 0x7f, 0xff, 0xff, 0xfc,
        0x38, 0x07, 0xe0, 0x00, 0x00, 0x07, 0xe0, 0x00, 0x00, 0x0f, 0x60, 0x00,
        0x00, 0x0f, 0x70, 0x00, 0x00, 0x0e, 0x70, 0x00, 0x00, 0x1e, 0x38, 0x00,
        0x00, 0x1e, 0x3c, 0x00, 0x00, 0x3c, 0x1c, 0x00, 0x00, 0x78, 0x1e, 0x00,
        0x00, 0x78, 0x0f, 0x00, 0x00, 0xf0, 0x07, 0xc0, 0x01, 0xe0, 0x07, 0xe0,
        0x07, 0xc0, 0x03, 0xfc, 0x0f, 0x00, 0x01, 0xfe, 0x3e, 0x00, 0x00, 0x7c,
        0x78, 0x00, 0x00, 0x38, 0x00, 0x00, 0x00, 0x00
    ],
    '气': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x00, 0x00,
        0x01, 0xf0, 0x00, 0x00, 0x01, 0xf0, 0x00, 0x00, 0x01, 0xe0, 0x00, 0x60,
        0x03, 0xc0, 0x00, 0xf0, 0x03, 0xff, 0xff, 0xf8, 0x07, 0x80, 0x03, 0x00,
        0x07, 0x80, 0x07, 0x80, 0x0f, 0xff, 0xff, 0xc0, 0x0e, 0x70, 0x00, 0x00,
        0x1e, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x07, 0x00, 0x3f, 0xff, 0xff, 0x80,
        0x77, 0x80, 0x07, 0x00, 0x60, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00,
        0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00,
        0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x8c,
        0x00, 0x00, 0x07, 0x8c, 0x00, 0x00, 0x03, 0x9c, 0x00, 0x00, 0x03, 0xdc,
        0x00, 0x00, 0x03, 0xfc, 0x00, 0x00, 0x01, 0xfc, 0x00, 0x00, 0x00, 0xfc,
        0x00, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x00, 0x00
    ],
    '美': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x1c, 0x00,
        0x00, 0x78, 0x3e, 0x00, 0x00, 0x7c, 0x3c, 0x00, 0x00, 0x3c, 0x38, 0x60,
        0x00, 0x3c, 0x71, 0xf0, 0x1f, 0xff, 0xff, 0xf8, 0x1e, 0x03, 0x80, 0x00,
        0x00, 0x03, 0x81, 0x80, 0x00, 0x03, 0x83, 0xc0, 0x0f, 0xff, 0xff, 0xe0,
        0x07, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x38,
        0x00, 0x03, 0x80, 0x7c, 0x7f, 0xff, 0xff, 0xfe, 0x38, 0x03, 0xc0, 0x00,
        0x00, 0x03, 0xc0, 0x60, 0x00, 0x07, 0x80, 0xf0, 0x3f, 0xff, 0xff, 0xf8,
        0x1c, 0x07, 0xc0, 0x00, 0x00, 0x0f, 0xe0, 0x00, 0x00, 0x0f, 0x70, 0x00,
        0x00, 0x1e, 0x78, 0x00, 0x00, 0x3c, 0x3e, 0x00, 0x00, 0x7c, 0x1f, 0x80,
        0x00, 0xf8, 0x0f, 0xf0, 0x03, 0xf0, 0x07, 0xfe, 0x1f, 0xc0, 0x01, 0xfc,
        0x7e, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x00
    ],
    '丽': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00, 0x3e, 0x7f, 0xff, 0xff, 0xfe,
        0x78, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1c, 0x0e, 0x70, 0x38,
        0x1f, 0xff, 0x7f, 0xfc, 0x1e, 0x0e, 0x70, 0x78, 0x1e, 0x0e, 0x70, 0x78,
        0x1e, 0x0e, 0x70, 0x78, 0x1f, 0x8e, 0x7c, 0x78, 0x1f, 0x8e, 0x7e, 0x78,
        0x1f, 0xce, 0x7e, 0x78, 0x1f, 0xee, 0x77, 0x78, 0x1e, 0xee, 0x77, 0xf8,
        0x1e, 0xfe, 0x77, 0xf8, 0x1e, 0xfe, 0x77, 0xf8, 0x1e, 0xfe, 0x73, 0xf8,
        0x1e, 0xfe, 0x73, 0xf8, 0x1e, 0x0e, 0x70, 0x78, 0x1e, 0x0e, 0x70, 0x78,
        0x1e, 0x0e, 0x70, 0x78, 0x1e, 0x0e, 0x70, 0x78, 0x1e, 0x0e, 0x70, 0x78,
        0x1f, 0xde, 0x76, 0x78, 0x1f, 0xfe, 0x77, 0xf8, 0x1e, 0x3e, 0x71, 0xf0,
        0x1c, 0x1c, 0x70, 0xf0, 0x00, 0x00, 0x00, 0x00
    ],
    '浙': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1c, 0x0e, 0x00, 0x00,
        0x1f, 0x0f, 0x00, 0x78, 0x0f, 0x0e, 0x3b, 0xfc, 0x0f, 0x0e, 0x3f, 0xfc,
        0x07, 0xce, 0x3c, 0x00, 0x07, 0xce, 0x3c, 0x00, 0x00, 0xcf, 0xfc, 0x00,
        0x61, 0xff, 0xfc, 0x00, 0x71, 0xfe, 0x3c, 0x0c, 0x7d, 0x8e, 0x3c, 0x1c,
        0x3f, 0x8e, 0x3f, 0xfe, 0x1f, 0x8e, 0x78, 0xe0, 0x1f, 0x8f, 0xf8, 0xe0,
        0x1f, 0x0f, 0xb8, 0xe0, 0x07, 0x3e, 0x38, 0xe0, 0x07, 0xfe, 0x38, 0xe0,
        0x07, 0xfe, 0x38, 0xe0, 0x0e, 0xee, 0x38, 0xe0, 0x0e, 0x0e, 0x38, 0xe0,
        0x7e, 0x0e, 0x78, 0xe0, 0x7e, 0x0e, 0x70, 0xe0, 0x1e, 0x0e, 0x70, 0xe0,
        0x1e, 0x0e, 0xf0, 0xe0, 0x1e, 0x0e, 0xe0, 0xe0, 0x1e, 0xff, 0xe0, 0xe0,
        0x1e, 0xff, 0xc0, 0xe0, 0x1e, 0x3f, 0x80, 0xe0, 0x1e, 0x1f, 0x80, 0xe0,
        0x00, 0x06, 0x00, 0xe0, 0x00, 0x00, 0x00, 0x00
    ],
    '江': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x1c, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x30, 0x0f, 0x80, 0x00, 0x78,
        0x07, 0xbf, 0xff, 0xfc, 0x07, 0xbc, 0x78, 0x00, 0x03, 0x70, 0x78, 0x00,
        0x60, 0x60, 0x78, 0x00, 0x78, 0xe0, 0x78, 0x00, 0x3c, 0xe0, 0x78, 0x00,
        0x1e, 0xc0, 0x78, 0x00, 0x1f, 0xc0, 0x78, 0x00, 0x0d, 0xc0, 0x78, 0x00,
        0x01, 0x80, 0x78, 0x00, 0x03, 0x80, 0x78, 0x00, 0x03, 0x80, 0x78, 0x00,
        0x07, 0x00, 0x78, 0x00, 0x07, 0x00, 0x78, 0x00, 0x4f, 0x00, 0x78, 0x00,
        0x7e, 0x00, 0x78, 0x00, 0x1e, 0x00, 0x78, 0x00, 0x0e, 0x00, 0x78, 0x00,
        0x0e, 0x00, 0x78, 0x1c, 0x1e, 0x00, 0x78, 0x3c, 0x1f, 0xff, 0xff, 0xfe,
        0x1f, 0xc0, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '杭': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x80, 0x60, 0x00,
        0x03, 0xc0, 0x78, 0x00, 0x03, 0x80, 0x3c, 0x00, 0x03, 0x80, 0x3c, 0x00,
        0x03, 0x80, 0x1c, 0x30, 0x03, 0x80, 0x1c, 0x78, 0x03, 0x8f, 0xff, 0xfc,
        0x03, 0xbf, 0x00, 0x00, 0x7f, 0xfc, 0x00, 0x00, 0x77, 0x80, 0x00, 0x00,
        0x07, 0x81, 0xc3, 0x80, 0x07, 0x81, 0xff, 0xc0, 0x07, 0xc1, 0xc3, 0x80,
        0x0f, 0xf1, 0xc3, 0x80, 0x0f, 0xf9, 0xc3, 0x80, 0x0f, 0xf9, 0xc3, 0x80,
        0x1f, 0xb9, 0xc3, 0x80, 0x1f, 0xb9, 0xc3, 0x80, 0x3b, 0x99, 0xc3, 0x80,
        0x3b, 0x81, 0xc3, 0x80, 0x73, 0x81, 0xc3, 0x80, 0x73, 0x83, 0xc3, 0x9c,
        0xe3, 0x83, 0xc3, 0x9c, 0x03, 0x87, 0x83, 0x9c, 0x03, 0x87, 0x83, 0x9e,
        0x03, 0x8f, 0x03, 0xfe, 0x03, 0x9e, 0x03, 0xfe, 0x03, 0xfc, 0x00, 0x00,
        0x03, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '州': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x70,
        0x00, 0xe0, 0xc0, 0x78, 0x00, 0xf0, 0xf0, 0x70, 0x00, 0xe0, 0xf0, 0x70,
        0x00, 0xe0, 0xe0, 0x70, 0x00, 0xe0, 0xe0, 0x70, 0x00, 0xe0, 0xe0, 0x70,
        0x01, 0xe0, 0xe0, 0x70, 0x01, 0xe0, 0xe0, 0x70, 0x0d, 0xf8, 0xec, 0x70,
        0x0d, 0xfc, 0xee, 0x70, 0x0d, 0xee, 0xef, 0x70, 0x1d, 0xcf, 0xe7, 0x70,
        0x3d, 0xcf, 0xe7, 0x70, 0x3d, 0xcf, 0xe7, 0x70, 0x3d, 0xce, 0xe6, 0x70,
        0x01, 0xc0, 0xe0, 0x70, 0x01, 0xc0, 0xe0, 0x70, 0x03, 0xc0, 0xe0, 0x70,
        0x03, 0xc0, 0xe0, 0x70, 0x03, 0x80, 0xe0, 0x70, 0x07, 0x80, 0xe0, 0x70,
        0x07, 0x80, 0xe0, 0x70, 0x0f, 0x00, 0xe0, 0x70, 0x0e, 0x00, 0xe0, 0x70,
        0x1e, 0x00, 0xc0, 0x70, 0x3c, 0x00, 0x00, 0x70, 0x78, 0x00, 0x00, 0x70,
        0x70, 0x00, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00
    ],
    '王': [    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x70,0x00,0x00,0x00,0xf8,0x1f,0xff,0xff,0xf8,0x0e,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0xc0,0x00,0x03,0xc1,0xe0,0x0f,0xff,0xff,0xf0,0x07,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x00,0x00,0x03,0xc0,0x18,0x00,0x03,0xc0,0x3c,0x7f,0xff,0xff,0xfe,0x38,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
],
    '燕': [    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1c,0x38,0x00,0x00,0x1e,0x3c,0x00,0x00,0x1c,0x38,0x30,0x00,0x1c,0x38,0x78,0x7f,0xff,0xff,0xfc,0x38,0x1c,0x38,0x00,0x00,0x1c,0x38,0x00,0x00,0x1c,0x38,0x00,0x01,0xdf,0xff,0x80,0x01,0xfc,0x3f,0x80,0x01,0xd8,0x07,0xb8,0x01,0xdc,0x77,0xf8,0x7f,0xdf,0xff,0xfc,0x39,0xdc,0x7f,0xe0,0x01,0xdc,0x77,0x80,0x01,0xdc,0x77,0x8c,0x03,0xdc,0x77,0x8c,0x1f,0xdc,0x77,0x8c,0x7f,0xdf,0xf7,0x9c,0x79,0xdc,0x7f,0xfe,0x71,0xd8,0x63,0xfe,0x01,0x80,0x00,0x00,0x06,0x30,0xe1,0xc0,0x06,0x38,0x70,0xf0,0x0e,0x3c,0x78,0xf8,0x0e,0x1e,0x3c,0x7c,0x1e,0x1e,0x3c,0x3c,0x3e,0x1e,0x1c,0x3c,0x3c,0x0e,0x1c,0x38,0x00,0x00,0x00,0x00
],
    '聆': [    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x1c,0x00,0x00,0x0f,0x1e,0x00,0xff,0xff,0x3e,0x00,0x7e,0x38,0x3e,0x00,0x0e,0x38,0x7f,0x00,0x0e,0x38,0x7f,0x00,0x0e,0x38,0x73,0x80,0x0e,0x38,0xf3,0xc0,0x0f,0xf9,0xf1,0xe0,0x0e,0x39,0xdd,0xf0,0x0e,0x3b,0xde,0xfc,0x0e,0x3f,0x8e,0x7e,0x0e,0x3f,0x0e,0x3c,0x0e,0x3e,0x0e,0x00,0x0f,0xf8,0x00,0x00,0x0e,0x38,0x00,0xe0,0x0e,0x3b,0xff,0xf0,0x0e,0x39,0xc1,0xf0,0x0e,0x3b,0x01,0xe0,0x0e,0x3f,0x03,0xc0,0x0f,0xfc,0x07,0x80,0x3f,0xf9,0xc7,0x00,0x7f,0x39,0xfe,0x00,0x7c,0x38,0x7c,0x00,0x30,0x38,0x3f,0x00,0x00,0x38,0x0f,0x80,0x00,0x38,0x07,0x80,0x00,0x38,0x03,0x80,0x00,0x38,0x01,0x80,0x00,0x00,0x00,0x00
],
    '': [],
}
FONT_24 = {
    'WIDTH':
    24,
    'HEIGHT':
    24,
    'SIZE':
    72,
    '当': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x60,
        0x1e, 0x38, 0xf0, 0x0f, 0x38, 0xf8, 0x07, 0xb9, 0xe0, 0x03, 0xb9, 0xc0,
        0x03, 0xbb, 0x80, 0x00, 0x3b, 0x1c, 0x3f, 0xff, 0xfc, 0x18, 0x00, 0x1c,
        0x00, 0x00, 0x1c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x1c, 0x0f, 0xff, 0xfc,
        0x0e, 0x00, 0x1c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x1c,
        0x3f, 0xff, 0xfc, 0x38, 0x00, 0x1c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00
    ],
    '前': [
        0x00, 0x00, 0x00, 0x03, 0x81, 0xc0, 0x01, 0xc3, 0xc0, 0x01, 0xe3, 0x80,
        0x00, 0xe7, 0x1c, 0x7f, 0xff, 0xfe, 0x70, 0x00, 0x00, 0x18, 0x60, 0x30,
        0x1f, 0xf7, 0x38, 0x1c, 0x77, 0xb0, 0x1c, 0x77, 0x30, 0x1c, 0x77, 0x30,
        0x1f, 0xf7, 0x30, 0x1c, 0x77, 0x30, 0x1c, 0x77, 0x30, 0x1c, 0x77, 0x30,
        0x1f, 0xf7, 0x30, 0x1c, 0x77, 0x30, 0x1c, 0x77, 0x30, 0x1c, 0x77, 0x30,
        0x1c, 0x73, 0xf0, 0x1f, 0xf3, 0xf0, 0x1c, 0xe0, 0xf0, 0x00, 0x00, 0x00
    ],
    '天': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x1f, 0xff, 0xf8,
        0x0c, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00,
        0x00, 0x38, 0x18, 0x00, 0x38, 0x3c, 0x7f, 0xff, 0xfe, 0x70, 0x7c, 0x00,
        0x00, 0x7e, 0x00, 0x00, 0x7e, 0x00, 0x00, 0xf7, 0x00, 0x00, 0xe7, 0x00,
        0x01, 0xe3, 0x80, 0x01, 0xc3, 0xc0, 0x03, 0x81, 0xe0, 0x07, 0x80, 0xf8,
        0x0e, 0x00, 0x7e, 0x3c, 0x00, 0x3f, 0x70, 0x00, 0x1c, 0x00, 0x00, 0x00
    ],
    '气': [
        0x00, 0x00, 0x00, 0x03, 0x80, 0x00, 0x07, 0x80, 0x00, 0x07, 0x00, 0x38,
        0x0f, 0xff, 0xfc, 0x0e, 0x00, 0x00, 0x1e, 0x00, 0xe0, 0x1f, 0xff, 0xf0,
        0x3b, 0x80, 0x00, 0x70, 0x01, 0xc0, 0xff, 0xff, 0xe0, 0xcc, 0x01, 0xc0,
        0x00, 0x01, 0xc0, 0x00, 0x01, 0xc0, 0x00, 0x01, 0xc0, 0x00, 0x01, 0xc0,
        0x00, 0x01, 0xc0, 0x00, 0x00, 0xe6, 0x00, 0x00, 0xee, 0x00, 0x00, 0xfe,
        0x00, 0x00, 0x7e, 0x00, 0x00, 0x7e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x00
    ],
    '美': [
        0x00, 0x00, 0x00, 0x03, 0x83, 0x80, 0x03, 0xc7, 0x80, 0x01, 0xe7, 0x00,
        0x00, 0xe7, 0x38, 0x3f, 0xff, 0xfc, 0x38, 0x38, 0x00, 0x00, 0x38, 0x70,
        0x1f, 0xff, 0xf8, 0x0c, 0x38, 0x00, 0x00, 0x38, 0x1c, 0xff, 0xff, 0xfe,
        0x70, 0x30, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x38, 0x38, 0x7f, 0xff, 0xfc,
        0x38, 0x7c, 0x00, 0x00, 0x7e, 0x00, 0x00, 0xe7, 0x00, 0x01, 0xe3, 0xc0,
        0x03, 0xc1, 0xfc, 0x1f, 0x00, 0xff, 0x7c, 0x00, 0x3c, 0x00, 0x00, 0x00
    ],
    '丽': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1e, 0xff, 0xff, 0xff,
        0x60, 0x00, 0x00, 0x30, 0x6e, 0x18, 0x3f, 0xff, 0xfc, 0x38, 0x76, 0x1c,
        0x38, 0x66, 0x1c, 0x3e, 0x67, 0x9c, 0x3e, 0x67, 0x9c, 0x3f, 0x67, 0xdc,
        0x3f, 0xe7, 0xfc, 0x3b, 0xe6, 0xfc, 0x3b, 0xe6, 0xfc, 0x3b, 0xe6, 0xfc,
        0x3b, 0x66, 0xdc, 0x38, 0x66, 0x1c, 0x38, 0x66, 0x1c, 0x38, 0x66, 0x1c,
        0x3f, 0xe7, 0xfc, 0x3b, 0xe6, 0xfc, 0x38, 0xee, 0x38, 0x00, 0x00, 0x00
    ],
    '浙': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x70, 0x1c, 0x3c, 0x77, 0x7e,
        0x1c, 0x73, 0xf8, 0x0f, 0x73, 0x00, 0x0f, 0x7f, 0x00, 0xc7, 0xff, 0x00,
        0xf7, 0xf3, 0x0e, 0x7e, 0x73, 0xff, 0x3e, 0x7f, 0x30, 0x3e, 0x7f, 0x30,
        0x0c, 0xff, 0x30, 0x1f, 0xf7, 0x30, 0x1f, 0xf7, 0x30, 0x3f, 0x77, 0x30,
        0xf8, 0x77, 0x30, 0x38, 0x7e, 0x30, 0x38, 0x7e, 0x30, 0x38, 0x7c, 0x30,
        0x3b, 0xfc, 0x30, 0x39, 0xf8, 0x30, 0x18, 0xf0, 0x30, 0x00, 0x00, 0x00
    ],
    '江': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x00, 0x00,
        0x1e, 0x00, 0x1c, 0x1f, 0xff, 0xfe, 0x0f, 0xc7, 0x00, 0xcf, 0x87, 0x00,
        0xf3, 0x07, 0x00, 0x7b, 0x07, 0x00, 0x3f, 0x07, 0x00, 0x3e, 0x07, 0x00,
        0x0e, 0x07, 0x00, 0x0e, 0x07, 0x00, 0x0c, 0x07, 0x00, 0x1c, 0x07, 0x00,
        0xfc, 0x07, 0x00, 0x3c, 0x07, 0x00, 0x18, 0x07, 0x00, 0x38, 0x07, 0x0e,
        0x3f, 0xff, 0xff, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
}
FONT_48 = {
    'WIDTH':
    24,
    'HEIGHT':
    48,
    'SIZE':
    144,
    '1': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x0c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0xfc, 0x00, 0x07, 0xfc, 0x00,
        0x07, 0xfc, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x7e, 0x00, 0x07, 0xff, 0xf0,
        0x07, 0xff, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '2': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x01, 0xff, 0x80, 0x07, 0xff, 0xe0, 0x0f, 0x83, 0xf0, 0x1f, 0x01, 0xf0,
        0x1e, 0x00, 0xf8, 0x1e, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x3f, 0x00, 0x78,
        0x3f, 0x00, 0x78, 0x3f, 0x00, 0x78, 0x1f, 0x00, 0xf8, 0x00, 0x00, 0xf8,
        0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0, 0x00, 0x03, 0xf0, 0x00, 0x03, 0xe0,
        0x00, 0x07, 0xc0, 0x00, 0x0f, 0x80, 0x00, 0x1f, 0x00, 0x00, 0x3e, 0x00,
        0x00, 0x7c, 0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0, 0x00, 0x03, 0xe0, 0x00,
        0x03, 0xc0, 0x00, 0x07, 0x80, 0x1c, 0x0f, 0x00, 0x1c, 0x1f, 0x00, 0x38,
        0x3e, 0x00, 0x38, 0x3c, 0x00, 0xf8, 0x3f, 0xff, 0xf8, 0x3f, 0xff, 0xf8,
        0x3f, 0xff, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '3': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x01, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x0f, 0x87, 0xe0, 0x1e, 0x03, 0xe0,
        0x1e, 0x01, 0xf0, 0x1e, 0x01, 0xf0, 0x1f, 0x00, 0xf0, 0x1f, 0x00, 0xf0,
        0x1f, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x01, 0xf0,
        0x00, 0x03, 0xe0, 0x00, 0x07, 0xc0, 0x00, 0x3f, 0x80, 0x00, 0xff, 0x00,
        0x00, 0xff, 0xc0, 0x00, 0x07, 0xe0, 0x00, 0x01, 0xf0, 0x00, 0x00, 0xf8,
        0x00, 0x00, 0xf8, 0x00, 0x00, 0x78, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c,
        0x1e, 0x00, 0x7c, 0x3f, 0x00, 0x7c, 0x3f, 0x00, 0x7c, 0x3f, 0x00, 0xf8,
        0x3e, 0x00, 0xf8, 0x1e, 0x01, 0xf0, 0x1f, 0x83, 0xe0, 0x0f, 0xff, 0xc0,
        0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '4': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x03, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x0f, 0xc0,
        0x00, 0x0f, 0xc0, 0x00, 0x1f, 0xc0, 0x00, 0x3f, 0xc0, 0x00, 0x3f, 0xc0,
        0x00, 0x7f, 0xc0, 0x00, 0xf7, 0xc0, 0x00, 0xe7, 0xc0, 0x01, 0xe7, 0xc0,
        0x01, 0xc7, 0xc0, 0x03, 0xc7, 0xc0, 0x07, 0x87, 0xc0, 0x07, 0x07, 0xc0,
        0x0f, 0x07, 0xc0, 0x1e, 0x07, 0xc0, 0x1c, 0x07, 0xc0, 0x3c, 0x07, 0xc0,
        0x38, 0x07, 0xc0, 0x7f, 0xff, 0xfe, 0x7f, 0xff, 0xfe, 0x7f, 0xff, 0xfe,
        0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0,
        0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x7f, 0xfe,
        0x00, 0x7f, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '5': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x0f, 0xff, 0xf8, 0x0f, 0xff, 0xf8, 0x0f, 0xff, 0xf8, 0x0e, 0x00, 0x00,
        0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00,
        0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x3f, 0x00,
        0x0f, 0xff, 0xc0, 0x0f, 0xff, 0xe0, 0x0f, 0xc3, 0xf0, 0x1f, 0x01, 0xf0,
        0x1e, 0x00, 0xf8, 0x1e, 0x00, 0xf8, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c,
        0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x1e, 0x00, 0x7c,
        0x3f, 0x00, 0x7c, 0x3f, 0x00, 0x78, 0x3f, 0x00, 0xf8, 0x3e, 0x00, 0xf8,
        0x3e, 0x00, 0xf8, 0x1e, 0x01, 0xf0, 0x0f, 0x83, 0xe0, 0x07, 0xff, 0xc0,
        0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '6': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x0f, 0xff, 0xf8, 0x0f, 0xff, 0xf8, 0x0f, 0xff, 0xf8, 0x0e, 0x00, 0x00,
        0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00,
        0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x3f, 0x00,
        0x0f, 0xff, 0xc0, 0x0f, 0xff, 0xe0, 0x0f, 0xc3, 0xf0, 0x1f, 0x01, 0xf0,
        0x1e, 0x00, 0xf8, 0x1e, 0x00, 0xf8, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c,
        0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x1e, 0x00, 0x7c,
        0x3f, 0x00, 0x7c, 0x3f, 0x00, 0x78, 0x3f, 0x00, 0xf8, 0x3e, 0x00, 0xf8,
        0x3e, 0x00, 0xf8, 0x1e, 0x01, 0xf0, 0x0f, 0x83, 0xe0, 0x07, 0xff, 0xc0,
        0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '7': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x1f, 0xff, 0xfc, 0x1f, 0xff, 0xfc, 0x1f, 0xff, 0xf8, 0x1f, 0x00, 0x78,
        0x1e, 0x00, 0x70, 0x1c, 0x00, 0xf0, 0x38, 0x00, 0xe0, 0x38, 0x01, 0xe0,
        0x00, 0x01, 0xc0, 0x00, 0x03, 0xc0, 0x00, 0x03, 0x80, 0x00, 0x07, 0x80,
        0x00, 0x07, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x1e, 0x00,
        0x00, 0x1e, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
        0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf8, 0x00,
        0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00,
        0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xf8, 0x00,
        0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '8': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x01, 0xff, 0x80, 0x07, 0xff, 0xe0, 0x0f, 0x83, 0xf0, 0x1f, 0x00, 0xf0,
        0x1e, 0x00, 0xf8, 0x3e, 0x00, 0x78, 0x3c, 0x00, 0x7c, 0x3c, 0x00, 0x7c,
        0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x78, 0x3f, 0x00, 0x78, 0x1f, 0x80, 0xf8,
        0x1f, 0xe0, 0xf0, 0x0f, 0xf3, 0xe0, 0x07, 0xff, 0xc0, 0x01, 0xff, 0x00,
        0x07, 0xff, 0xc0, 0x0f, 0x9f, 0xe0, 0x1f, 0x0f, 0xf0, 0x1e, 0x03, 0xf8,
        0x3e, 0x01, 0xf8, 0x3c, 0x00, 0xfc, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c,
        0x78, 0x00, 0x3c, 0x7c, 0x00, 0x3c, 0x7c, 0x00, 0x7c, 0x3c, 0x00, 0x7c,
        0x3e, 0x00, 0x78, 0x1f, 0x00, 0xf8, 0x0f, 0x83, 0xf0, 0x07, 0xff, 0xe0,
        0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '9': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x03, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x0f, 0x83, 0xe0, 0x1f, 0x01, 0xf0,
        0x1e, 0x00, 0xf0, 0x3e, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x3c, 0x00, 0x78,
        0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c,
        0x7c, 0x00, 0x7c, 0x7c, 0x00, 0xfc, 0x3e, 0x00, 0xfc, 0x3e, 0x01, 0xfc,
        0x3f, 0x03, 0xfc, 0x1f, 0x87, 0xfc, 0x1f, 0xff, 0xfc, 0x07, 0xff, 0x7c,
        0x03, 0xfc, 0x7c, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xf8,
        0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0, 0x0f, 0x01, 0xf0, 0x1f, 0x01, 0xe0,
        0x1f, 0x03, 0xe0, 0x1f, 0x07, 0xc0, 0x1f, 0x8f, 0x80, 0x0f, 0xff, 0x00,
        0x07, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '0': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0xff, 0x00, 0x03, 0xff, 0xc0, 0x07, 0xe7, 0xe0, 0x07, 0xc3, 0xe0,
        0x0f, 0x81, 0xf0, 0x1f, 0x80, 0xf0, 0x1f, 0x00, 0xf8, 0x1f, 0x00, 0xf8,
        0x3e, 0x00, 0xf8, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c,
        0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c,
        0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c,
        0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c,
        0x3e, 0x00, 0xf8, 0x1f, 0x00, 0xf8, 0x1f, 0x00, 0xf8, 0x1f, 0x00, 0xf0,
        0x0f, 0x81, 0xf0, 0x07, 0xc3, 0xe0, 0x07, 0xe7, 0xe0, 0x03, 0xff, 0xc0,
        0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    ':': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0xfe, 0x00,
        0x00, 0xfe, 0x00, 0x00, 0xfe, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x7c, 0x00, 0x00, 0xfe, 0x00, 0x00, 0xfe, 0x00, 0x00, 0xfe, 0x00,
        0x00, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '-': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7f, 0xff, 0xfe,
        0x7f, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
    '/': [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x0e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x3c,
        0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00, 0x70, 0x00, 0x00, 0xf0,
        0x00, 0x00, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xc0, 0x00, 0x03, 0xc0,
        0x00, 0x03, 0x80, 0x00, 0x07, 0x80, 0x00, 0x07, 0x80, 0x00, 0x07, 0x00,
        0x00, 0x0f, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1c, 0x00,
        0x00, 0x3c, 0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00, 0x70, 0x00,
        0x00, 0xf0, 0x00, 0x00, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xc0, 0x00,
        0x03, 0xc0, 0x00, 0x03, 0x80, 0x00, 0x07, 0x80, 0x00, 0x07, 0x00, 0x00,
        0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00,
        0x1c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00,
        0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ],
}
