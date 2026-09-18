package entitys;
import mob.Mob;
public class Skeleton extends Mob{
    private int arrows = 16;
    private int id;

    public Skeleton(){
        super("Skeleton", 100, 20);
        this.id = Mob.getNumberEntitys();
    }

    public void attack() {
        this.arrows--;
    }

    public int getId() {
        return id;
    }
}
