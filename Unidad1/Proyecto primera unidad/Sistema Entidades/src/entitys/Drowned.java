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
