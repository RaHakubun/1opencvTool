import cv2
import numpy as np
def hhds_test():
    # 任务1：利用numpy绘制一张800*800*3的全黑图像,类型为uint8
    ###########Begin###########
    img = np.zeros([800, 800, 3], dtype=np.uint8)

    ###########End#############

    # 任务2：绘制一条起始坐标400,0到0,400的绿色宽20xp的直线
    ###########Begin###########
    cv2.line(img, (400, 0), (0, 400), (0, 255, 0), 20)

    ###########End#############

    # 任务3：绘制一个起始坐标128,128终止坐标512,512宽5xp的白色矩阵
    ###########Begin###########
    cv2.rectangle(img, (128, 128), (512, 512), (255, 255, 255), 5)
    ###########End#############

    # 任务4：绘制一个实心黄色圆形 圆心坐标(512, 512)圆直径128黄色(0,255,255)的闭合图形
    ###########Begin###########
    cv2.circle(img, (512, 512), 128, (0, 255, 255), -1)
    ###########End#############

    # 任务5：绘制青色半椭圆椭圆中心坐标(256, 700)长轴和短轴长度(128, 64)椭圆沿逆时针方向旋转的角度(0)椭圆弧顺时针方向起始的角度(0)椭圆弧顺时针方向结束的角度(360)颜色(255,255,0)闭合图形
    ###########Begin###########
    cv2.ellipse(img, (256, 700), (128, 64), 0, 0, 360, (255, 255, 0), -1)
    ###########End#############

    # data是图像坐标
    data = [[501, 689], [290, 399], [709, 247], [625, 252]]
    # 任务6：绘制多边形颜色为紫色(255,0,255)
    ###########Begin###########
    pts = np.array(data, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], 1, (255, 0, 255), 1)
    ###########End#############

    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    # 任务7: 加入文字文字内容 educoder文字左下角起始坐标(10,100)字体font文字大小(4)白色粗细(2)线类型

    ###########Begin###########
    cv2.putText(img, "educoder", (10, 100), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    ###########End#############
    return img
def COLOR_SPACE_HSV(path):
    image = cv2.imread(path)  # 根据路径读取一张图片
    #####Begin#####
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    cv2.imshow("./HSV色彩空间/H.jpg", h)
    cv2.waitKey(0)
    cv2.imshow("./HSV色彩空间/S.jpg", s)
    cv2.waitKey(0)
    cv2.imshow("./HSV色彩空间/V.jpg", v)
    cv2.waitKey(0)
    low_hsv = np.array([0, 0, 0])
    # 上限
    high_hsv = np.array([200, 40, 100])
    # 滤值
    dst = cv2.inRange(hsv, low_hsv, high_hsv)
    #####End#####
    print(np.sum(dst))
    return h,s,v
def COLOR_SPACE_RGB(path):
    img = cv2.imread(path)
    #####Begin######
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    cv2.imwrite('./RGB色彩空间/b.jpg', b)
    cv2.imwrite('./RGB色彩空间/g.jpg', g)
    cv2.imwrite('./RGB色彩空间/r.jpg', r)
    if np.max(b) > 100:
        b = b * (255 / np.max(b))
    binary_output = np.zeros_like(b)
    binary_output[((b > 90) & (b <= 230))] = 255
    ######End######
    print(np.sum(binary_output))
    return r,g,b

def and_operation(path1,path2):
    # 读取灰度图像
    X = cv2.imread(path1, 0)
    Y = cv2.imread(path2, 0)
    # 任务1：X,Y 进行与运算
    ########## Begin ##########
    result = X & Y
    ##########  End  ##########
    # 将结果写入路径
    print(np.sum(result))
    return result

