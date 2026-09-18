package entitys;
import mob.Mob;
public class Creeper extends Mob {
    protected int id;

    public Creeper(){
        super("Creeper", 80, 15);
        this.id = Mob.getNumberEntitys();
    }
    public void attack(){
        System.out.println("...💥");
        die();
    }

    public int getId() {
        return id;
    }

}
