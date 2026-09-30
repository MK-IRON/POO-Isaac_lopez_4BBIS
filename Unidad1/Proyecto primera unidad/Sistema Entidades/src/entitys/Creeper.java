package entitys;
import mob.Mob;
public class Creeper extends Mob {
    protected int id;

    public Creeper(){
        super("Creeper", 80, 15);
        this.id = Mob.getNumberEntitys();
    }
    public String attack(){
        die();
        return"...💥";
    }

    public int getId() {
        return id;
    }

}
