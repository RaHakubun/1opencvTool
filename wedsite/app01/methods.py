from cv2 import Laplacian
import numpy as np
import cv2
import math

#                  {%url ''%}
### 计算处理
# 逻辑与
def and_operation(path1, path2):
    X = cv2.imread(path1)
    Y = cv2.imread(path2)
    X = cv2.resize(X, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    Y = cv2.resize(Y, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    result = X & Y
    print(np.sum(result))
    return result


# 逻辑或
def or_operation(path1, path2):
    X = cv2.imread(path1)
    Y = cv2.imread(path2)
    X = cv2.resize(X, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    Y = cv2.resize(Y, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    result = X | Y
    print(np.sum(result))
    return result


# 逻辑非
def not_operation(path1):
    X = cv2.imread(path1)
    result = ~X
    print(np.sum(result))
    return result


# 加法运算
def ope_add(path1, path2):
    X = cv2.imread(path1)
    Y = cv2.imread(path2)
    X = cv2.resize(X, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    Y = cv2.resize(Y, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    result = cv2.add(X, Y)
    print(np.sum(result))
    return result


# 减法运算
def ope_subtract(path1, path2):
    X = cv2.imread(path1)
    Y = cv2.imread(path2)
    X = cv2.resize(X, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    Y = cv2.resize(Y, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    result = cv2.subtract(X, Y)
    print(np.sum(result))
    return result


# 乘法运算
def ope_multiply(path1, path2):
    X = cv2.imread(path1)
    Y = cv2.imread(path2)
    X = cv2.resize(X, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    Y = cv2.resize(Y, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    result = cv2.multiply(X, Y)
    print(np.sum(result))
    return result


# 除法运算
def ope_divide(path1, path2):
    X = cv2.imread(path1)
    Y = cv2.imread(path2)
    X = cv2.resize(X, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    Y = cv2.resize(Y, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    result = cv2.divide(X, Y)
    print(np.sum(result))
    return result


### 几何变换
# 翻转
def Flip(path1):
    src = cv2.imread(path1, 1)
    # 水平镜像
    horizontal = cv2.flip(src, 1)
    # 垂直镜像
    vertical = cv2.flip(src, 0)
    # 对角镜像 ，并保存
    cross = cv2.flip(src, -1)
    return cross


# 仿射变换
def affine_trans(path1):
    # 获取图像shape
    src = cv2.imread(path1, 1)
    rows, cols = src.shape[: 2]
    post1 = np.float32([[50, 50], [200, 50], [50, 200]])
    post2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(post1, post2)
    result = cv2.warpAffine(src, M, (rows, cols))
    return result


### 形态学
# 腐蚀
def erosion(path):
    src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    erosion = cv2.erode(src, kernel)
    return erosion


# 膨胀
def dilation(path):
    src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    dilation = cv2.dilate(src, kernel)
    return dilation


# 开运算
def morph_open(path):
    src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    open = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
    return open


# 闭运算
def morph_close(path):
    src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10), (-1, -1))
    dilation = cv2.dilate(src, kernel)
    close = cv2.erode(dilation, kernel)
    return close


### 图像增强
## 空域平滑
# 邻域平均法
def neighbor_aver(path):
    img = cv2.imread(path, 1)
    result = cv2.blur(img, (5, 5))
    return result


# 中值滤波法
def median_filter(path):
    img = cv2.imread(path, 1)
    result = cv2.medianBlur(img, 5)
    return result


## 空域锐化
# Roberts梯度算子
def roberts(path):
    img = cv2.imread(path, 0)
    height, width = img.shape[:2]
    result = np.zeros((height, width))
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            result[i][j] = np.abs(img[i][j] - img[i + 1][j + 1]) + np.abs(img[i + 1][j] - img[i][j + 1])
    return result


def sobel(path):
    img = cv2.imread(path, 0)
    height, width = img.shape[:2]
    result = np.zeros((height, width))
    s_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    s_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    for i in range(0, height - 2):
        for j in range(0, width - 2):
            result[i + 1, j + 1] = np.abs(np.sum(img[i:i + 3, j:j + 3] * s_x)) + np.abs(
                np.sum(img[i:i + 3, j:j + 3] * s_y))
    return np.uint8(result)


# Prewitt梯度算子
def prewitt(path):
    img = cv2.imread(path, 0)
    height, width = img.shape[:2]
    result = np.zeros((height, width))
    for i in range(1, height - 2):
        for j in range(1, width - 2):
            f_y = np.sum(2*(img[i:i + 3, j:j + 3][2])/2 - np.sum(img[i:i + 3, j:j + 3][0]/2))
            f_x = np.sum(2*(img[i:i + 3, j:j + 3][:, 2])/2 - np.sum(img[i:i + 3, j:j + 3][:, 0]/2))
            if np.abs(f_y)/2 + np.abs(f_x)/2 > 255/2:
                result[i][j] = 255
            else:
                result[i][j] = np.abs(f_y) + np.abs(f_x)
    return result

# Laplacian算子
def laplacian(path):
    img = cv2.imread(path, 0)
    height, width = img.shape[:2]
    result = np.zeros((height, width))
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    result = cv2.filter2D(img, -1, kernel)
    return result


# 频域平滑
# 理想低通滤波器
# def lowpass_filter(path):
#     img=cv2.imread(path,0)
#     src=np.fft.fft2(img)
#     src_shift=np.fft.fftshift(src)
#     #src_trans=20*np.log(np.abs(src_c))
#     height,width=img.shape[:2]
#     u=np.floor(height/2)
#     v=np.floor(width/2)
#     img_trans=np.zeros((height,width))
#     d0=90
#     for i in range(height):
#         for j in range(width):
#             d = np.sqrt((i-u)**2 + (j-v)**2)
#             if d<=d0:
#                 img_trans[i][j]=1
#     #iimg_trans=src_c*img_trans
#     iimg_trans=np.multiply(src_shift,img_trans)
#     iimg_shift=np.fft.ifftshift(iimg_trans)
#     iimg=np.fft.ifft2(iimg_shift)
#     img_back=np.abs(iimg)
#     #img_back=np.real(iimg)
#     img_back=(img_back-np.amin(img_back))/(np.amax(img_back)-np.amin(img_back))
#     return img_back



# 巴特沃斯低通滤波器
def butterworth_low_filter(path):
    img = cv2.imread(path, 0)
    src = np.fft.fft2(img)
    src_shift = np.fft.fftshift(src)
    # src_trans=20*np.log(np.abs(src_c))
    height, width = img.shape[:2]
    u = np.floor(height / 2)
    v = np.floor(width / 2)
    img_trans = np.zeros((height, width))
    d0 = 90
    rank = 2
    for i in range(height):
        for j in range(width):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            img_trans[i][j] = 1 / (1 + 0.414 * (d / d0) ** (2 * rank))
    # iimg_trans=src_c*img_trans
    iimg_trans = np.multiply(src_shift, img_trans)
    iimg_shift = np.fft.ifftshift(iimg_trans)
    iimg = np.fft.ifft2(iimg_shift)
    img_back = np.abs(iimg)
    # img_back=np.real(iimg)
    img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
    return img_back


## 频域锐化
# 理想高通滤波器
def highpass_filter(path):
    img = cv2.imread(path, 0)
    src = np.fft.fft2(img)
    src_shift = np.fft.fftshift(src)
    # src_trans=20*np.log(np.abs(src_c))
    height, width = img.shape[:2]
    u = np.floor(height / 2)
    v = np.floor(width / 2)
    img_trans = np.zeros((height, width))
    d0 = 90
    for i in range(height):
        for j in range(width):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            if d > d0:
                img_trans[i][j] = 1
    # iimg_trans=src_c*img_trans
    iimg_trans = np.multiply(src_shift, img_trans)
    iimg_shift = np.fft.ifftshift(iimg_trans)
    iimg = np.fft.ifft2(iimg_shift)
    img_back = np.abs(iimg)
    # img_back=np.real(iimg)
    img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
    return img_back


# 巴特沃斯高通滤波器
def butterworth_high_filter(path):
    img = cv2.imread(path, 0)
    src = np.fft.fft2(img)
    src_shift = np.fft.fftshift(src)
    # src_trans=20*np.log(np.abs(src_c))
    height, width = img.shape[:2]
    u = np.floor(height / 2)
    v = np.floor(width / 2)
    img_trans = np.zeros((height, width))
    d0 = 90
    rank = 2
    for i in range(height):
        for j in range(width):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            img_trans[i][j] = 1 / (1 + 0.414 * (d0 / d) ** (2 * rank))
    # iimg_trans=src_c*img_trans
    iimg_trans = np.multiply(src_shift, img_trans)
    iimg_shift = np.fft.ifftshift(iimg_trans)
    iimg = np.fft.ifft2(iimg_shift)
    img_back = np.abs(iimg)
    # img_back=np.real(iimg)
    img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
    return img_back


### 边缘检测
# Roberts算子
def robs(path):
    img = cv2.imread(path, 0)
    # 2. Roberts算子
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    # 3. 卷积操作
    x = cv2.filter2D(img, cv2.CV_16S, kernelx)
    y = cv2.filter2D(img, cv2.CV_16S, kernely)
    # 4. 数据格式转换
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    return Roberts


# Sobel算子
# def sob(path):
#     img = cv2.imread(path, 0)
#     # 2. Roberts算子
#     kernelx = cv2.Sobel(img, cv2.CV_16S, 1, 0)
#     kernely = cv2.Sobel(img, cv2.CV_16S, 0, 1)
#     # 3. 卷积操作
#     x = cv2.filter2D(img, cv2.CV_16S, kernelx)
#     y = cv2.filter2D(img, cv2.CV_16S, kernely)
#     # 4. 数据格式转换
#     absX = cv2.convertScaleAbs(x)
#     absY = cv2.convertScaleAbs(y)
#     Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
#     return Sobel


def sob(filepath):
    # 读取图像
    img = cv2.imread(filepath)
    ########## Begin ##########
    # 1. 灰度化处理图像
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. 求Sobel 算子
    x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)  # 对x求一阶导
    y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)  # 对y求一阶导

    # 3. 数据格式转换
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    # 4. 组合图像
    Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    return Sobel
    ########## End ##########
    # 保存图像


# Laplacian算子
def lap(path):
    # 1.读取图像
    img = cv2.imread(path, 0)
    # 2. 高斯滤波
    img = cv2.GaussianBlur(img, (5, 5), 0, 0)
    # 3. 拉普拉斯算法
    dst = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
    # 4. 数据格式转换
    Laplacian = cv2.convertScaleAbs(dst)
    return Laplacian


# LoG边缘算子
def log(path):
    # 1.读取图像
    img = cv2.imread(path, 0)
    # 2. 边缘扩充处理图像并使用高斯滤波处理该图像
    image = cv2.copyMakeBorder(img, 2, 2, 2, 2, borderType=cv2.BORDER_REPLICATE)
    image = cv2.GaussianBlur(image, (3, 3), 0, 0)
    # 3. 使用Numpy定义LoG算子
    m1 = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])
    # 4. 卷积运算
    # 为了使卷积对每个像素都进行运算，原图像的边缘像素要对准模板的中心。
    # 由于图像边缘扩大了2像素，因此要从位置2到行(列)-2
    image1 = np.zeros(image.shape)
    rows = image.shape[0]
    cols = image.shape[1]
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            image1[i, j] = np.sum(m1 * image[i - 2:i + 3, j - 2:j + 3])
    # 5. 数据格式转换
    image1 = cv2.convertScaleAbs(image1)
    return image1


def cny(path):
    filepath = path
    # 读取图像
    src = cv2.imread(filepath)
    ########## Begin ##########
    # 1. 高斯滤波
    blur = cv2.GaussianBlur(src, (3, 3), 0)
    # 2. 灰度转换
    image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # 3. 求x，y方向的Sobel算子
    gradx = cv2.Sobel(image, cv2.CV_16SC1, 1, 0)
    grady = cv2.Sobel(image, cv2.CV_16SC1, 0, 1)
    # 4. 使用Canny函数处理图像，x,y分别是3求出来的梯度，低阈值50，高阈值150
    edge_output = cv2.Canny(gradx, grady, 50, 150)
    ########## End ##########
    return edge_output


### 图像噪声
# 噪声描述器
def noise_desc(path):
    image = cv2.imread(path, 0)
    output = np.zeros(image.shape, np.uint8)
    # 遍历图像，获取叠加噪声后的图像
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] < 100:
                # 添加食盐噪声
                output[i][j] = 255
            elif image[i][j] > 200:
                # 添加胡椒噪声
                output[i][j] = 0
            else:
                # 不添加噪声
                output[i][j] = image[i][j]
    print(np.sum(output))
    return output


# 均值类滤波器
def aver_filter(path):
    image = cv2.imread(path, 0)
    output = np.zeros(image.shape, np.uint8)
    # 遍历图像，进行均值滤波
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # 计算均值,完成对图片src的几何均值滤波
            ji = 1.0
            for n in range(-1, 2):
                # 防止越界  
                if 0 <= j + n < image.shape[1]:
                    ji *= image[i][j + n]
            output[i][j] = int(math.pow(ji, 1 / 3))

            # 滤波器的大小为1*3

            ######### End #########
    # 展示均值滤波后的图片
    return output


# 排序统计类滤波器
def sort_filter(path):
    image = cv2.imread(path, 0)
    # 待输出的图片
    output = np.zeros(image.shape, np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # 最大值滤波器
            max = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    # 防止越界  
                    if 0 <= i + m < image.shape[0] and 0 <= j + n < image.shape[1]:
                        if max < image[i + m][j + n]:
                            max = image[i + m][j + n]
                            # 更新最大值
            output[i][j] = max
    return output


# 选择性滤波器
def opt_filter(path):
    image = cv2.imread(path, 0)
    output = np.zeros(image.shape, np.uint8)
    max = 200
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] <= max:
                output[i][j] = 0
            else:
                output[i][j] = image[i][j]
    return output


### 图像进阶
# 线条变化检测
def line_change(path):
    img = cv2.imread(path)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    # 使用HoughLines算法  
    # rho为1  
    # theta为np.pi/2  
    # threshold为 118  
    # 其他的默认  
    #########  Begin #########  
    lines = cv2.HoughLines(edges, 1, np.pi / 2, 118)
    #########  end  ##########
    result = img.copy()
    for i_line in lines:
        for line in i_line:
            rho = line[0]
            theta = line[1]
            if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):  # 垂直直线  
                pt1 = (int(rho / np.cos(theta)), 0)
                pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
                cv2.line(result, pt1, pt2, (0, 0, 255))
            else:
                pt1 = (0, int(rho / np.sin(theta)))
                pt2 = (result.shape[1], int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
                cv2.line(result, pt1, pt2, (0, 0, 255), 1)
    minLineLength = 200
    maxLineGap = 15
    # 使用HoughLinesP算法  
    # rho为1  
    # theta为np.pi/2  
    # threshold为 118  
    # 并设置上面提供的minLineLength和maxLineGap
    #########  Begin #########  
    linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength, maxLineGap)
    #########  end  ##########
    result_P = img.copy()
    for i_P in linesP:
        for x1, y1, x2, y2 in i_P:
            cv2.line(result_P, (x1, y1), (x2, y2), (0, 255, 0), 3)
    return result_P


# path = 'static/img/hongwen.jpg'
# img = lowpass_filter(path)
# cv2.imshow('right?', img)
# cv2.waitKey(0)
