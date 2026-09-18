package main;
import entitys.*;
import mob.Mob;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        //=== List declarations ====
        List<Mob> mobList = new ArrayList<>();

        //=== MAIN WHILE ====
        while(true){
            int opt = mainMenu(sc);
            if(opt == 1){
                createMob(sc,mobList);
            }
            else if(opt == 2){
            killMob(mobList, sc);
            }
            else if(opt == 3){

            }
            else if(opt == 4){
                getMobs(mobList, sc);
            }
            else if(opt == 5){
            System.exit(0);
            }
        }
    }

    public static int mainMenu(Scanner sc){
        System.out.println("\t...::: WELCOME TO MINECRAFT :::...\n" +
                "\nWhat are we going to do?" +
                "\n(1).-Create mob" +
                "\n(2).-Kill mob" +
                "\n(3).-Describe a mob" +
                "\n(4).-Take a look at the mobs"+
                "\n(5).-Exit");
        return sc.nextInt();
    }

    public static void createMob(Scanner sc, List<Mob> mobList){
        System.out.println("Select the mob: " +
                "\n(1).-Skeletons" +
                "\n(2).-Creeper" +
                "\n(3).-Zombie" +
                "\n(4).-Drowned" +
                "\n(5).-Exit");

        int opt = sc.nextInt();
        if(opt == 1){ //Create a skeleton
            mobList.add(new Skeleton());
        }
        if(opt == 2){ //Create a creper
            mobList.add(new Creeper());
        }
        if(opt == 3){ //Create a zombie
            mobList.add(new Zombie());
        }
        if(opt == 4){ //Create a drowned
            mobList.add(new Drowned());
        }
    }

    public static void killMob(List<Mob> mobList, Scanner sc){
        while(true) {
            System.out.println("Type the id of the mob: ");
            int opt = sc.nextInt();
            if (opt > 0 && opt <= Mob.getNumberEntitys()) {
                mobList.remove(opt - 1);
                Mob.setNumberEntitys(Mob.getNumberEntitys()-1);
                break;
            } else {
                System.out.println("Please select an existent mob");
            }
        }
    }

    public static void describeMob(){

    }

    public static void getMobs(List<Mob> mobList, Scanner sc){
        System.out.println("Number of entitys: " + Mob.getNumberEntitys());
        for(int i = 0; i < mobList.size(); i++){
            System.out.println(mobList.get(i).getName() + " ID: " + mobList.get(i).getId());
        }
        System.out.println("Press enter to continue");
        sc.nextLine();
    }
}
