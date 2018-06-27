GAME_CENTER_GET_SPEC = {
    'tags': ['게임 센터'],
    'description': '특정 게임 센터의 조회, 기본적으로는 전체 검색을 기반의 조회를 실행하며, 쿼리를 통한 세부 검색 가능',
    'parameters': [
        {
            'name': 'city_name',
            'description': '게임 센터가 위치한 도시 이름 (EX: 서울, 대전, 경기/북부, 강원, 세종 ... 등등)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'center_name',
            'description': '게임 센터의 점포 이름 (EX: 가오스, 매직캠프, 에이스 ... 등등)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'center_address',
            'description': '게임 센터의 도로명 주소 (EX: 대전광역시 동구 용운로, 서울특별시 용산구 ... 등등)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'game_name',
            'description': '게임 센터에 현재 있는 게임 기체의 이름',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'target_lng',
            'description': '위치 기반 조회를 위한 현재 사용자의 위치 정보 중 경도값',
            'in': 'query',
            'type': 'float',
            'required': False
        },

        {
            'name': 'target_lat',
            'description': '위치 기반 조회를 위한 현재 사용자의 위치 정보 중 위도값',
            'in': 'query',
            'type': 'float',
            'required': False
        },

        {
            'name': 'search_radius',
            'description': '위치 기반 조회를 위한 현재 사용자의 미터 단위 탐색 반경',
            'in': 'query',
            'type': 'int',
            'required': False
        },
    ],

    'responses': {
        '200': {
            'description': '성공 ([위도: 36.326468, 경도: 127.452524] 주위 반경 3km 내에 있는 오락실 목록)',
            'examples': {
                'application/json': [
                    {
                        "id": "5af2d442a9378e1c4c4c8254",
                        "city": "대전",
                        "name": "매직 캠프 게임스테이션",
                        "kind": "ⓚ",
                        "address": "대전 동구 동대전로 149",
                        "location": [
                            127.4464272,
                            36.3353801
                        ],
                        "opening": "11:00 ~ 23:00?"
                    },
                    {
                        "id": "5af2d441a9378e1c4c4c8253",
                        "city": "대전",
                        "name": "놀이터 오락실",
                        "kind": "ⓝ",
                        "address": "대전광역시 동구 동대전로 167 지하 1층",
                        "location": [
                            127.4473043,
                            36.3368919
                        ],
                        "opening": "11:00am~02:00am"
                    },
                    {
                        "id": "5af2d448a9378e1c4c4c8258",
                        "city": "대전",
                        "name": "가오스 게임장",
                        "kind": "ⓚⓝⓢ",
                        "address": "대전광역시 중구 중앙로 164번길 22-12 지하 1층",
                        "location": [
                            127.427557,
                            36.328302
                        ],
                        "opening": "10:00~24:00 ",
                    },
                    {
                        "id": "5af2d444a9378e1c4c4c8255",
                        "city": "대전",
                        "name": "테마 게임장",
                        "kind": "ⓝ",
                        "address": "대전광역시 동구 충정로 12",
                        "location": [
                            127.4523121,
                            36.3485708
                        ],
                        "opening": "변동이 많고 불규칙적"
                    }
                ]
            }
        }
    }
}