<<<<<<< HEAD
package entitys;

import mob.Mob;

public class Zombie extends Mob {
    protected int id;

    public Zombie(){
        super("Zombie", 100, 10);
        this.id = Mob.getNumberEntitys();
    }

    protected Zombie(String name, int hp, int speed){
        super(name,hp,speed);
    }

    public String attack(){
        return "Zombie give us a bite...Auch!";
    }

    public int getId() {
        return id;
    }
}
=======
package entitys;

import mob.Mob;

public class Zombie extends Mob {
    protected int id;

    public Zombie(){
        super("Zombie", 100, 10);
        this.id = Mob.getNumberEntitys();
    }

    protected Zombie(String name, int hp, int speed){
        super(name,hp,speed);
    }

    public void attack(){
        System.out.println("Zombie give us a bite...Auch!");
    }

    public int getId() {
        return id;
    }
}
>>>>>>> 9829f8d (Add turn_off(), add a new device class, upgrade gui (activity log))
