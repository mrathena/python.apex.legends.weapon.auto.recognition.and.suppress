
grab = 'grab'
save = 'save'
arms = 'arms'
arms1 = 'arms1'
arms2 = 'arms2'
mode = 'mode'
name = 'name'
game = 'game'
test = 'test'
data = 'data'
pixel = 'pixel'
pixel1 = 'pixel1'
pixel2 = 'pixel2'
cheat = 'cheat'
color = 'color'
point = 'point'
index = 'index'
detect = 'detect'  # 发现
bullet = 'bullet'  # 子弹
backpack = 'backpack'  # 背包
positive = 'positive'  # 肯定的
negative = 'negative'  # 否定的

light = 'light'  # 轻型弹药武器
heavy = 'heavy'  # 重型弹药武器
energy = 'energy'  # 能量弹药武器
sniper = 'sniper'  # 狙击弹药武器
shotgun = 'shotgun'  # 霰弹枪弹药武器
airdrop = 'airdrop'  # 空投武器

config = {
    "3440:1440": {
        grab: {  # 截图配置, 便于定位武器名称/武器模式的特征点(用于取色判断)
            save: 'C:\\Users\\mrathena\\Desktop\\grab',  # 截图存放路径
            arms1: [2944, 1381, 175, 26],  # 武器1的截图范围, xywh, 截图时需选到对应的武器
            arms2: [3139, 1380, 175, 26],  # 武器2的截图范围
            mode: []  # 武器模式的截图范围
        },
        cheat: {  # 作弊配置
            detect: {  # 辨别检测
                game: [  # 判断是否在游戏中
                    {
                        point: (236, 1344),  # 点的坐标, 血条左上角
                        color: 0x00FFFFFF  # 点的颜色, 255, 255, 255
                    },
                    {
                        point: (2947, 217),  # 性能参数左下角
                        color: 0x00FFFFFF
                    },
                    {
                        point: (2692, 1372),  # 生存物品右下角
                        color: 0x959595  # 149, 149, 149
                    }
                ],
                backpack: {  # 背包状态, 有无武器, 选择的武器
                    pixel1: {  # 像素点1
                        point: (),
                        color: 1
                    },
                    pixel2: {
                        point: (),
                        color: 1
                    }
                },
                mode: {  # 武器模式, 全自动/半自动/单发
                    pixel1: {  # 像素点1
                        point: (),
                        color: 1
                    },
                    pixel2: {
                        point: (),
                        color: 1
                    }
                },
                bullet: {  # 子弹类型
                    pixel: {
                        point: (),
                        color: 1
                    },
                    negative: [],  # 不需要压枪的颜色, 狙和喷子
                    '棕色': light,  # 轻型弹药武器
                    'dark green': heavy,  # 重型弹药武器
                    'light green': energy,  # 能量弹药武器
                    'dark blue': sniper,  # 狙击弹药武器
                    '喷子色': shotgun,  # 霰弹枪弹药武器
                    'airdrop': airdrop  # 空投武器
                },
                name: {  # 武器名称判断
                    light: [],
                    heavy: [],
                    energy: [],
                    sniper: [],
                    shotgun: [],
                    airdrop: []
                }
            },
            data: {
                airdrop: []  # 空投武器
            }
        }
    },
    "2560:1440": {

    },
    "2560:1080": {

    },
    "1920:1080": {

    }
}