package java;

class Main {
  public static void main(String[] args) {
    printData(fullName("Kate", "Jones"), 27);

    // fullNameメソッドを用いて、printDataの引数を書き換え
    printData(fullName("John", "Christopher", "Smith"), 65);
  }

  public static void printData(String name, int age) {
    System.out.println("私の名前は" + name + "です");
    System.out.println("年齢は" + age + "歳です");
  }

  public static String fullName(String firstName, String lastName) {
    return firstName + " " + lastName;
  }

  // fullNameメソッドを定義
  public static String fullName(String firstName, String middleName, String lastName) {
    return firstName + " " + middleName + " " + lastName;
  }
}
