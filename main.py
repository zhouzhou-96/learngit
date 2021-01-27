# -*- coding: utf-8 -*-
"""
代码模板说明:
(1)测试数据将会以一个字典的形式传递进入main函数。字典的格式为{"MapData":((), (), (),...), "TestPoint":((), (), (),...)}
(2)地图信息(MapData)的内容是一个存储着地图中每个点的阻挡或者非阻挡的实际情况的二维列表,如((1, 0, 1, 0, 1...), (0, 1, 1, 0, 1...),...)。其中阻挡点为1，非阻挡点为0
(3)测试点数据(TestPoint)的内容是一个存储着坐标点信息的二维列表,二维列表中的每个小列表的内容代表着坐标点的x,y坐标,即(x, y).测试点数据(TestPoint)格式如:((2, 4), (7, 9), (11, 8),...)
(4)玩家需要在main函数里面进行编写自己的逻辑代码，即可以自己编写类、函数等模块在main函数内进行调用,辅助计算出满足赛题要求的结果
(5)在main函数逻辑结束前，必须要返回从TestPoint中筛选出全部处于最大闭合区域的坐标的一个列表,格式与测试点数据格式相同,是个二维列表,如：
TestPoint = ((15, 1), (2, 12), (5, 3), (18, 11), (13, 11), (16, 7), (3, 8), (5, 2), (18, 10), (19, 11), (1, 8)),
而通过计算获得符合要求的点有:(5, 3), (16, 7), (5, 2),最终从main函数将会返回一个((5, 3), (16, 7), (5, 2))二维列表,即return ((5, 3), (16, 7), (5, 2))
(6)python代码的运行环境是python 3, 不支持python的外部依赖包，只支持python标准库
(7)不要使用全局变量进行计算相关数据的存储和计算。可以使用局部变量、类的成员变量等方式替代全局变量的使用
(8)坐标原点(0, 0)是地图信息(MapData)二维列表中第一行,第一列的元素,即oMap.m_MapData[0][0],之后地图将会向右、向下依次进行坐标(x, y)的递增。第x行、第y列的坐标是oMap.m_MapData[x-1][y-1]
"""

dInfo = {
    "MapData": (
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1),
        (1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1),
        (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1),
        (1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1),
        (1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    ),
    "TestPoint": (
        (16, 15),
        (18, 4),
        (13, 2),
        (5, 2),
        (4, 12),
        (14, 2)
    )
}


class CMap(object):
    def __init__(self):
        self.m_iWidth = 0
        self.m_iHeight = 0
        self.m_MapData = []
        self.m_TestPoint = []

    def SetData(self, mapData):
        """
        m_MapData[x][y]为坐标(x,y)的阻挡信息
        :param mapData:
        :return:
        """
        self.m_MapData = mapData
        self.m_iWidth = len(mapData[0])   # 地图宽
        self.m_iHeight = len(mapData)     # 地图高
        print self.m_iWidth, self.m_iHeight
        self.m_lMap = [[-1] * self.m_iWidth for i in range(self.m_iHeight)]  # 区域(x, y)所对应的id
        print len(self.m_lMap[0]), len(self.m_lMap)
        self.m_dHash = {}  # 区域id所对应的坐标{id: [(x1, y1), (x2, y2), ...], }
        self.m_iWeight = 0  # 区域最大权值

    def IsBlock(self, x, y):
        """
        采用笛卡尔坐标系
        :param x:横坐标
        :param y:纵坐标
        :return:0:表示非阻挡，1表示阻挡
        """
        return self.m_MapData[x][y]

    def SetTestPoint(self, testPoint):
        """
        用于测试是否在最大闭合区域的点
        :param testPoint:
        :return:
        """
        self.m_TestPoint = map(tuple, testPoint)

    def ParseMap(self):
        import copy
        w, h = self.m_iWidth, self.m_iHeight
        dHash = self.m_dHash
        lMap = self.m_lMap
        iWeight = 0
        # 遍历整个地图
        for i in range(h):
            for j in range(w):
                bIsBlock = self.m_MapData[i][j]
                if bIsBlock:
                    continue
                iId = i * w + j  # 坐标映射id
                dHash[iId] = [(i, j)]
                # 边界判断
                if i == 0 and j == 0:
                    lMap[i][j] = iId
                    continue
                if i == 0:
                    bLeft = self.m_MapData[i][j - 1]
                    # 向左合并
                    if not bLeft:
                        iLeftId = lMap[i][j - 1]
                        self.merge(iLeftId, iId)
                    else:
                        lMap[i][j] = iId
                    continue
                if j == 0:
                    bTop = self.m_MapData[i - 1][j]
                    # 向上合并
                    if not bTop:
                        iTopId = lMap[i - 1][j]
                        self.merge(iTopId, iId)
                    else:
                        lMap[i][j] = iId
                    continue

                bTop = self.m_MapData[i - 1][j]
                bLeft = self.m_MapData[i][j - 1]
                # 向左合并
                if not bTop:
                    iTopId = lMap[i - 1][j]
                    dHash[iId] = [(i, j)]
                    self.merge(iTopId, iId)
                    iId = iTopId
                else:
                    lMap[i][j] = iId

                # 向上合并
                if not bLeft:
                    iLeftId = lMap[i][j - 1]
                    self.merge(iLeftId, iId)
                else:
                    lMap[i][j] = iId

                iLen = len(dHash.get(iId, []))
                if iWeight < iLen:
                    iWeight = iLen
        self.m_iWeight = iWeight

    def merge(self, iId1, iId2):
        # 合并两个连通图,把iId1的标记给iId2
        if iId1 == iId2:
            return
        dHash = self.m_dHash
        lMap = self.m_lMap
        l1 = dHash.get(iId1, [])
        l2 = dHash.get(iId2, [])

        for item in l2:
            x,y = item
            lMap[x][y] = iId1

        dHash[iId1].extend(dHash[iId2])
        del dHash[iId2]

    def printf(self):
        for i in range(self.m_iHeight):
            for j in range(self.m_iWidth):
                iId = self.m_lMap[i][j]
                iWeight = len(self.m_dHash.get(iId, []))
                self.m_lMap[i][j] = iWeight
        for i in range(self.m_iHeight):
            print self.m_lMap[i]
        print self.m_iWeight
        for x, y in self.m_TestPoint:
            print x, y, self.m_lMap[x][y]
        # for i in xrange(self.m_iHeight):
        #     for j in xrange(self.m_iWidth):

    @classmethod
    def CreateMap(cls, dInfo):
        """
        地图数据的加载
        :param fpath:
        """
        mapData = dInfo.get("MapData", [])  # 获得地图信息
        testPoint = dInfo.get("TestPoint", [])  # 获得测试点数据
        oMap = CMap()
        oMap.SetData(mapData)
        oMap.SetTestPoint(testPoint)
        return oMap


def main(argv):
    oMap = CreateMap(argv)
    #####玩家代码开始编写#####
    oMap.ParseMap()
    oMap.printf()
    return ((5, 3), (16, 7), (5, 2))  # 返回结果示例


def CreateMap(dInfo):
    return CMap.CreateMap(dInfo)


if __name__ == '__main__':
    main(dInfo)