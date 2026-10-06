<<<<<<< HEAD
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
=======
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
>>>>>>> 9829f8d (Add turn_off(), add a new device class, upgrade gui (activity log))
