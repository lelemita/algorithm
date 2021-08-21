
// 코딩테스트 연습 > 월간 코드 챌린지 시즌2 >음양 더하기
// https://programmers.co.kr/learn/courses/30/lessons/76501
function solution(absolutes, signs) {
    let answer = 0;
    for (let i=0; i<signs.length; i++) {
        if (signs[i]) {
            answer += absolutes[i]
        } else {
            answer -= absolutes[i]
        }
    }
    return answer;
}

console.log(solution([4,7,12], [true,false,true]))