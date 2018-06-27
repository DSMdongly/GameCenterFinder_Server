GAME_GET_SPEC = {
    'tags': ['게임'],
    'description': '특정 게임 센터의 게임 목록을 조회',
    'parameters': [
        {
            'name': 'center_id',
            'description': '게임 센터의 고유 id값 게임 센터 JSON 의 id 값',
            'in': 'query',
            'type': 'str',
            'required': True
        },
    ],

    'responses': {
        '200': {
            'description': '성공, (가오스 게임장에 존재하는 게임 목록) [id: 5af2d448a9378e1c4c4c8258]',
            'examples': {
                'application/json': [
                    {
                        "name": "beatmania IIDX 25 CANNON BALLERS",
                        "price": "1000원",
                        "count": "1대",
                        "etc": "선곡시간 60초, 이어폰 앰프 설치"
                    },
                    {
                        "name": "EZ2AC : TIME TRAVELER",
                        "price": "500원",
                        "count": "1대",
                        "etc": None
                    },
                    {
                        "name": "리플렉 비트 유구의 리플레시아",
                        "price": "500원",
                        "count": "1대",
                        "etc": "이어폰 앰프 설치"
                    },
                    {
                        "name": "사운드 볼텍스 IV 헤븐리 헤이븐",
                        "price": "500원",
                        "count": "2대",
                        "etc": "플레이 가격 전 모드 동일  리얼 제네레이터 2대"
                    },
                    {
                        "name": "유비트 클랜",
                        "price": "LIGHT : 1 CREDIT  STANDARD : 2 CREDIT  PREMIUM : 3 CREDIT",
                        "count": "2대",
                        "etc": "500원 2크레딧  좌측기기 엠프장착"
                    },
                    {
                        "name": "노스텔지어 FORTE",
                        "price": "500원",
                        "count": "1대",
                        "etc": None
                    },
                    {
                        "name": "팝픈뮤직 토끼와 고양이와 소년의 꿈",
                        "price": "500원",
                        "count": "1대",
                        "etc": None
                    },
                    {
                        "name": "펌프 잇 업 PRIME 2",
                        "price": "500원",
                        "count": "3대",
                        "etc": "TX, LX 기체 각각 1대TX 기체 SD 해상도,스톡 5개, 2 스테이지 게이지 OFF,비트 온 1대, 스톡 5개"
                    },
                    {
                        "name": "maimai MiLK",
                        "price": "1000원",
                        "count": "2대",
                        "etc": "대전에서 유일하게 보유중"
                    },
                    {
                        "name": "MÚSECA 1+1/2",
                        "price": "500원",
                        "count": "1대",
                        "etc": None
                    },
                    {
                        "name": "신 태고의 달인",
                        "price": "500원",
                        "count": "1대",
                        "etc": "북 교체"
                    },
                    {
                        "name": "철권 7 FR",
                        "price": "400원",
                        "count": "7기",
                        "etc": "점포 내 대전 불가"
                    },
                    {
                        "name": "철권 6 BR",
                        "price": "300원",
                        "count": "2조",
                        "etc": None
                    },
                    {
                        "name": "철권 태그 토너먼트 2",
                        "price": "300원",
                        "count": "2조",
                        "etc": "네트워크 미연결"
                    },
                    {
                        "name": "완간 미드나이트 맥시멈 튠 5DX+",
                        "price": "1000원",
                        "count": "2조",
                        "etc": "지폐 사용 가능, 대전 유일"
                    },
                    {
                        "name": "타임 크라이시스 5",
                        "price": "1,000원",
                        "count": "1대",
                        "etc": None
                    },
                    {
                        "name": "미션 크래프트",
                        "price": "500원?",
                        "count": "1대",
                        "etc": None
                    },
                    {
                        "name": "각종 고전 게임들",
                        "price": "500원",
                        "count": "약 5대",
                        "etc": None
                    },
                    {
                        "name": "더★비시바시",
                        "price": "500원",
                        "count": "1대",
                        "etc": "지폐사용가능"
                    },
                    {
                        "name": "부스형 동전노래방",
                        "price": "500원 2곡1000원 4곡",
                        "count": "약 5대 이상",
                        "etc": "TJ S60F"
                    },
                    {
                        "name": "인형뽑기",
                        "price": "500원",
                        "count": "약 4대",
                        "etc": None
                    }
                ]
            }
        },

        '204': {
            'description': '게임 센터 조회 실패, 유효하지 않은 게임 센터의 ID'
        }
    }
}