This solution is for java.
i am adding 2 methods of this solution.

Method 1:
public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int j = 0 ; j<t ; j++) {
            char[] a = scan.next().toCharArray();
            String b = "";
            String c = "";
            for (int i = 0; i < a.length; i++) {
                // Print even chars
                if (i % 2 == 0) {
                    b = b + a[i];
                }
                // Print odd chars
                else {
                    c = c + a[i];
                }
            }
            System.out.print(b + " " + c);
            System.out.println("");
        }
        scan.close();
        
Method 2:
public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testCases = scan.nextInt();
        for(int i = 0; i < testCases; i++){
            char[] inputString = scan.next().toCharArray();
			
            // Print even chars
            for(int j = 0; j < inputString.length; j += 2){
                System.out.print(inputString[j]);
            }
            System.out.print(" ");
            
            // Print odd chars
            for(int j = 1; j < inputString.length; j += 2){
                System.out.print(inputString[j]);
            }
            System.out.println();
        }
        scan.close();
