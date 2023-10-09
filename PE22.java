import java.io.*;
import java.util.ArrayList;

public class PE22 {
    public static void main(String[] args) {
        ArrayList<String> sortedFirstLetter = new ArrayList<>();
        File file = new File("names.txt");
        FileReader fr = null;
        BufferedReader br = null;
        try {
            fr = new FileReader(file);
            br = new BufferedReader(fr);
            String line = br.readLine();
            line = line.substring(1, line.length() - 1);
            String[] names = line.split("\",\"");
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}