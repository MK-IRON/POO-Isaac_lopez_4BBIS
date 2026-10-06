<<<<<<< HEAD
package entitys;

import mob.Mob;

public class Drowned extends Zombie{
    protected int id;

    public Drowned(){
        super("Drowned" ,100, 20);
        this.id = Mob.getNumberEntitys();
    }

    @Override
    public int getId() {
        return id;
    }
    public String attack(){
        return"Drowned give us a bite...Auch";
    }
}
=======
package entitys;

import mob.Mob;

public class Drowned extends Zombie{
    protected int id;

    public Drowned(){
        super("Drowned" ,100, 20);
        this.id = Mob.getNumberEntitys();
    }

    @Override
    public int getId() {
        return id;
    }
    public void attack(){
        System.out.println("Drowned give us a bite...Auch");
    }
}
>>>>>>> 9829f8d (Add turn_off(), add a new device class, upgrade gui (activity log))
