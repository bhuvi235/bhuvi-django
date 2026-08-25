import java.util.Scanner;

public class StudentGradeCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter student name: ");
        String name = sc.nextLine();

        System.out.print("Enter number of subjects: ");
        int n = sc.nextInt();

        int[] marks = new int[n];
        int total = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Enter marks for subject " + (i + 1) + " (out of 100): ");
            marks[i] = sc.nextInt();
            total += marks[i];
        }

        double average = (double) total / n;
        char grade = getGrade(average);

        System.out.println("\n----- RESULT -----");
        System.out.println("Student Name : " + name);
        System.out.println("Total Marks  : " + total + " / " + (n * 100));
        System.out.printf("Average      : %.2f%n", average);
        System.out.println("Grade        : " + grade);

        sc.close();
    }

    static char getGrade(double avg) {
        if (avg >= 90) return 'A';
        else if (avg >= 75) return 'B';
        else if (avg >= 60) return 'C';
        else if (avg >= 40) return 'D';
        else return 'F';
    }
}