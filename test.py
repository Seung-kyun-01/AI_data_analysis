# 지속적인 커밋: 코드를 수정할 때마다 git add .와 git commit -m "메시지"를 습관화하면 프로젝트의 버전 관리를 아주 안전하게 할 수 있습니다

import pandas as pd

data = {
    "사원이름": ["강승균", "김철수", "이영희"],
    "부서": ["빅데이터팀", "회계팀", "인사팀"],
    "직급": ["사원", "대리", "과장"],
}
df = pd.DataFrame(data)
print(df)
