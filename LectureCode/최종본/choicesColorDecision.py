from random import randint, choice


class ChoicesColorDecision:

    def decide(self, diffi, colorcode):  # 파라미터: 난이도(1 ~ 5), 색상코드
        self.r, self.g, self.b = [int(colorcode[i:i + 2], 16) for i in (0, 2, 4)]
        self.colorList = []
        self.diffi = diffi
        self.variance = (6 - self.diffi) * 50  # 편차의 합 (편차의 정도, 작을수록 어려워짐)

        for color in range(11):
            deviList = [0, 0, 0]  # 편차 3개가 담길 리스트

            # deviList 내의 원소의 합이 self.variance가 되도록 무작위 생성
            while sum(deviList) != self.variance:
                for i in range(len(deviList)):
                    if self.variance > 128:
                        deviList[i] = randint(0, 128)
                    else:
                        deviList[i] = randint(0, self.variance)

            pn = [-1, 1]
            color_rgb = [self.r, self.g, self.b]

            # 무작위 부호가 적용된 편차를 r, g, b 각각에 더하는 반복문
            for i, origin in zip(range(len(color_rgb)), color_rgb):

                # 필터링: 0 ~ 255 범위를 벗어나지 않는 부호가 적용될 때까지 반복
                while True:
                    color_rgb[i] = origin + deviList[i] * choice(pn)
                    if 0 < color_rgb[i] < 255:
                        break

            other = "%02x%02x%02x" % tuple(color_rgb)
            self.colorList.append(other)

        self.colorList.insert(randint(0, 11), colorcode)
        return self.colorList


if __name__ == '__main__':
    colors = ChoicesColorDecision()
    print(colors.decide(5, "9F6256"))