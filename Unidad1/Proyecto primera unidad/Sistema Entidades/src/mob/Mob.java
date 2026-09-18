package mob;

public abstract class Mob {
    private String name;
    private int hp;
    private int speed;
    private static int numberEntitys = 0;

    public Mob(String name, int hp, int speed){
        this.name = name;
        this.hp = hp;
        this.speed = speed;
        numberEntitys++;
    }

    public abstract void attack();
    public abstract int getId();

    //============
    //=== GET ====
    //============

    public String getName() {
        return name;
    }

    public int getHp() {
        return hp;
    }

    public int getSpeed() {
        return speed;
    }

    public static int getNumberEntitys() {
        return numberEntitys;
    }

    public boolean getState(){
       return this.hp > 0;
    }

    //============
    //=== SET ====
    //============

    public void setHp(int hp) {
        this.hp = hp;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void die(){
        this.hp = 0;
    }

    public static void setNumberEntitys(int numberEntitys) {
        Mob.numberEntitys = numberEntitys;
    }
}
