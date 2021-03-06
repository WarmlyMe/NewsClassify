# encoding=utf-8
import numpy as np

from bayes.naive_bayes.test_word_matrix import get_test_essay_matrix, get_matrix_by_string
from bayes_classifier import BayesClassifier

from bayes.naive_bayes.utils import *

if __name__ == '__main__':

    print("读取数据-------------------------")
    # 不用读取数据

    print("开始训练-------------------------")
    # 新建分类器对象
    bayes_classifier = BayesClassifier()
    # print(bayes_classifier.prior_probability)
    # print(bayes_classifier.conditional_probability[0][0])
    print("开始测试-------------------------")
    # 读取测试数据

    # 向量化特征
    # features = None
    # cates = None

    # 进行预测
    features = get_test_essay_matrix('../data/测试.xls')
    # print(features[0][1000])
    # print(bayes_classifier.prior_probability.reshape(10, 1))
    # print(bayes_classifier.conditional_probability[0][10:30])
    res = bayes_classifier.predict(features)

    # 结果比较
    # print("分类的正确结果是：", cates)
    # print("预测的分类结果是：", res)
    answer = get_essay_type("../data/测试.xls")
    print(answer)
    print(res)
    print(str('f1_score=')+str(get_score(answer, res)))

    # str="所罗门群岛外交部长马内列8日开始的对台访问，俨然被蔡英文当作救命稻草。在这之前，这个太平洋岛国要与台湾“断交”的消息，已经传了四五个月。尤其令台当局坐立不安的是，近日率部长级小组来大陆后，所罗门群岛议员阿戈瓦卡带回国的信息是“该交个新朋友了”。9日，蔡英文在与马内列见面时，对所罗门群岛大加称赞，并签了一系列合作协议。台湾“外交部长”吴钊燮声称，这番互动对于深化“台所邦谊”具有重大意义，却被台湾《中国时报》讽刺，台“外交部”很可能又是半夜吹口哨，为自己壮胆。前有几内亚比绍领导人一面访台，一面和北京接触，后有台方早知萨尔瓦多要“断交”，还坚称“邦交笃睦”，将一次访问说成“邦交稳定”的信号，台当局大概很心虚。如果所罗门群岛与台湾“断交”，将成为蔡英文任上的第六个“断交国”。而更让台当局忧心的是，在太平洋地区的6个台湾“邦交国”中，所罗门群岛面积最大、人口最多，“断交”可能在该地区引发连锁效应。“台湾拼命避免再次丢掉‘邦交国’。”第一个身体力行法新社所说的“拼命”，就是蔡英文。9日上午，蔡英文在“总统府”会见马内列夫妇。她称所罗门群岛“一直是台湾在国际上非常坚定的朋友”，热络表示“好朋友就应该要常常相聚，而台湾与所罗门群岛就是最佳的例子”。法新社称，蔡英文说这番话时，这个太平洋岛国正在认真考虑是否放弃台湾，转而与更具经济实力的北京建立外交关系。蔡英文显然试图力劝所罗门不要这样做。蔡英文向马内列强调，台湾是“负责任、肯奉献的伙伴”，希望所罗门群岛“在国际上继续大力支持台湾”，称未来台湾将与所罗门群岛共同努力，进一步提升双边关系。有岛内分析人士告诉《环球时报》记者，近几年，台湾为挽留所罗门群岛可谓下了血本。蔡英文上任不久，台湾就承诺资助2800万美元帮该国兴建2023年太平洋运动会场馆。自今年4月下旬所罗门群岛举行大选后，台所关系不稳的消息接连传出。5月，再次当选总理的索加瓦雷表示新政府正重新考虑与台湾当局之间的关系。之后，该国成立跨党派评估小组，评估与台湾的关系，并前往与北京建交的太平洋岛国考察。英国路透社近日报道说，8月中旬，由所罗门群岛部长和总理私人秘书组成的部长小组，已与北京直接接触。台湾《联合报》9日援引知情人士的消息称，在所罗门群岛大选之后，台“外交部”针对该国每位国会议员进行地毯式说明沟通，并在必要时说明若与北京建交的状况，让他们有“正确认识”。为平衡情势，台“外交部”此次力邀所罗门群岛“亮点人物”到访。民进党“立委”王定宇乐观判断，称马内列访台是双方“邦交稳定的信号”。9日下午，马内列在与吴钊燮举行媒体见面会时说，双方签了很多协议，包括太平洋运动会场馆的合作计划。台湾《联合晚报》称，所国外交部次长科林·贝克告诉媒体，“台所关系目前一切照旧”，但也没有在双方关系上说死，仅表示该国政府有一套检视外交政策的机制。台港澳法研究中心执行主任李晓兵9日对《环球时报》记者说，台当局不停地在所谓“邦交国”上进行“外交投资”，勉强维系关系，这种行动本身就证明了“邦交稳定”是无稽之谈。事实上，“邦交国”无法证明台湾的国际地位，无非是台当局欺骗岛内民众的伎俩。"
    # features = get_matrix_by_string('rre',str)
    # res = bayes_classifier.predict(features)
    # print(res)

    #获取分类总数
    # workbook = xlrd.open_workbook('../data/源数据.xls')
    #
    # all_news = np.zeros(10)
    # for table in workbook:
    #     all_news[table.number] = table.nrows
    # all_news = all_news[:9]
    # print(all_news)
    # np.save("先验概率矩阵", all_news)





