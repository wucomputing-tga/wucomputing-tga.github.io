import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        //Create new list of students
        List<Student> students = new ArrayList<>();
        //add student alice with id A1
        students.add(new Student("Alice", "A1"));
        //add student bob with id B2
        students.add(new Student("Bob", "B2"));
        //add student charlie with id c3
        students.add(new Student("Charlie", "C3"));

        //Create new list of courses
        List<Course> courses = new ArrayList<>();
        //add the new course Java Programming
        courses.add(new Course("Java Programming"));
        //add the new course Database management
        courses.add(new Course("Database Management"));

        //Register each student for one of the two courses
        for (int i = 0; i < students.size(); i++) {
            Student student = students.get(i);
            student.registerForCourse(courses.get(i % 2));
        }

        //Print out the course and all of the students enrolled
        for (Course course : courses) {
            System.out.println(course.getName() + " enrolled students: " + course.getStudents());
        }
    }
}

class Student {
    private String name;
    private String id;
    private List<Course> courses;

    public Student(String name, String id) {
        this.name = name;
        this.id = id;
        this.courses = new ArrayList<>();
    }

    public void registerForCourse(Course course) {
        if (!courses.contains(course)) {
            //add course to student
            courses.add(course);
            //add student to course
            course.addStudent(this);
        }
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public List<Course> getCourses() {
        return courses;
    }

    public String toString() {
        return name + " (" + id + ")";
    }
}

class Course {
    private String name;
    private List<Student> students;

    public Course(String name) {
        this.name = name;
        this.students = new ArrayList<>();
    }

    public void addStudent(Student student) {
        if (!students.contains(student)) {
            //add student to course
            students.add(student);
            //add course to student
            student.registerForCourse(this);
        }
    }

    public String getName() {
        return name;
    }

    public List<Student> getStudents() {
        return students;
    }

    public String toString() {
        return name;
    }
}

