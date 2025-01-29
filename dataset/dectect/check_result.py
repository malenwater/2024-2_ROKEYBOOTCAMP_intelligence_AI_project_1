import os

# 디렉터리 경로 설정
true_result_path = './results/True_result'
result_path = './results/01/result'

# 파일 리스트를 비교할 변수들
same_files = []  # 같은 파일들
different_files = []  # 다른 파일들

# 폴더 내 모든 파일 목록 가져오기
true_result_files = os.listdir(true_result_path)
result_files = os.listdir(result_path)
# 같은 이름의 파일을 비교
for file in true_result_files:
    if file in result_files:
        # 파일 경로 설정
        true_file_path = os.path.join(true_result_path, file)
        result_file_path = os.path.join(result_path, file)
        
        # 파일 내용 읽기
        with open(true_file_path, 'r') as true_file:
            true_content = true_file.read()
        
        with open(result_file_path, 'r') as result_file:
            result_content = result_file.read()
        
        # 내용 비교
        if true_content == result_content:
            same_files.append(file)
        else:
            different_files.append(file)

# 출력 결과
total_files = len(same_files) + len(different_files)
print(f"총 파일 개수: {total_files}")
print(f"같은 파일 개수: {len(same_files)}")
print(f"다른 파일 개수: {len(different_files)}")
different_files.sort()
# 다른 파일 출력
if different_files:
    print("\n다른 파일들:")
    for file in different_files:
        print(file)
