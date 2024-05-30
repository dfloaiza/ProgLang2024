import java.util.concurrent.locks.*;

/**
 * Clase que implementa métodos de sincronización de hilos:
 * a) métodos sincronizados
 * b) candados intrínsecos
 * c) variables volátiles
 * @author loaiz
 *
 */
public class GameResourceManagement {
	
	//RECURSO COMPARTIDO
	//(a) sincronizar la variable dando acceso atómico con "volatile":
	private volatile int coins = 0;
	

	//(b) método sincronizado:
	public synchronized void collectCoins(int amount)	
	{
		System.out.println("Jugador "+Thread.currentThread().getName() + " está recolectando "+amount+" monedas");		
		coins += amount;
		System.out.println("El jugador ahora tiene "+coins+" monedas");		
	}
	
	//(c) candado
	private final Lock spendLock = new ReentrantLock();
	
	
	public void spendCoins(int amount)
	{
		spendLock.lock();
		if(coins >= amount)
		{
			coins -= amount;
			System.out.println("El jugador "+ Thread.currentThread().getName() +" ahora tiene "+coins+" monedas");
			Thread.currentThread().sl
		}
		else
		{
			System.out.println("El jugador "+ Thread.currentThread().getName() +" no puede gastar monedas.");
		}
		spendLock.unlock();
		
	}
	
	public int checkCoinsBalance()
	{
		return coins;
	}
	
	
	public static void main(String[] args)	
	{
		
		GameResourceManagement myGameRM = new GameResourceManagement();
		
		Thread player1 = new Thread(
					() -> {
						myGameRM.collectCoins(100);
					}
				);
		
		Thread player2 = new Thread(
					() -> {
						myGameRM.spendCoins(10);
					}
				);
		
		Thread player3 = new Thread(
					()-> {
						myGameRM.checkCoinsBalance();
					}
				);				
				
		try {
			player1.start();
			player1.join();
			
			player2.start();
			player2.join();
			
			player3.start();
			player3.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Balance final de recursos:"+myGameRM.checkCoinsBalance());		
		
	}
	
}
