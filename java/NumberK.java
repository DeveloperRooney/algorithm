import java.util.Arrays;

public class NumberK {

    public static void main(String[] args) {


        NumberKSolution sol = new NumberKSolution();

        int[] array = {1,5,2,6,3,7,4};

        int[][] commands = {{2,5,3}, {4,4,1}, {1,7,3}};
        

        int[] arr = sol.solution(array, commands);

        for (int x = 0; x < arr.length; x++) {
            System.out.print(arr[x] + " ");
        }


    }

}

class NumberKSolution {


    // 정수가 담긴 1차원 배열 array와 각 인덱스에 총 세 개의 정수가 담긴 2차원 배열 commands를
    // 입력 받아 commands의 각 인덱스에 있는 세 자리 숫자 중 첫번째 숫자부터 두번째 숫자까지의 인덱스로 array를 잘라내고 정렬한 후
    // commands의 각 인덱스 중 마지막 숫자번째에 있는 array의 숫자를 반환하는 메소드를 생성
    public int[] solution(int[] array, int[][] commands) {

        // answer라는 1차원 배열을 입력받은 commands 길이만큼 생성한다.
        int[] answer = new int[commands.length];

        // commands의 길이만큼 반복
        for(int i =0; i<commands.length; i++) {

            // array 배열의 commands[i][0]-1부터 commands[i][1] 만큼 복사하여 배열을 생성한다.
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1,commands[i][1]);
            
            // 자바의 내장 함수 Arrays의 sort()를 사용하여 오름차순 정렬
            Arrays.sort(temp);

            // temp 배열의 'commands 각 인덱스 중 마지막 인덱스에 있는 정수번째 인덱스' 를 answer[i]에 넣어준다. 
            answer[i]=temp[commands[i][2]-1];
        }

        return answer;
    }
}
