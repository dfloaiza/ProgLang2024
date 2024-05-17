
public class SimpleThreads {

	SynchronizedCounter sharedResource1;
	IntrinsicLockObject sharedResource2;
	AtomicAccessSynch sharedResource2;
		
	static void threadMessage(String msg ){
		String threadName = Thread.currentThread().getName();
		System.out.format("%s: %s%n", threadName, msg);
	}	
	
	private static class MessageLoop implements Runnable{

		@Override
		public void run() {
			// TODO Auto-generated method stub
			String messages[] = {
				"Lenguajes",
				"de",
				"programación",
				"2024A","clase","de","hilos","con","runnable"
			};
			
			try{
				for(String s:messages){
					Thread.sleep(4000);
					threadMessage(s);
				}
			}
			catch(InterruptedException e){
				threadMessage("No he terminado de ejecutar!");
			}			
		}		
	}	
	
	public static void main(String[] args) throws InterruptedException
	{
		long tiempoEspera = 1000*60*60, elapsedTime = 0L;
				
		threadMessage("Iniciando loop de mensajes...");
		//se captura tiempo de inicio del hilo:
		long startTime = System.currentTimeMillis();
		
		//iniciamos solo un hilo:
		Thread unHilo = new Thread(new MessageLoop());
		unHilo.start();
		
		threadMessage("Esperando a que el hilo termine...");
		
		while(unHilo.isAlive())
		{
			threadMessage("Esperando aún...");
			unHilo.join(1000);
			//se obtiene el tiempo transcurrido desde que inició:
			elapsedTime = System.currentTimeMillis() - startTime;
			if(elapsedTime > tiempoEspera && unHilo.isAlive())
			{
				threadMessage("Se está demorando mucho!");
				unHilo.interrupt();
				unHilo.join();
			}			
		}
		threadMessage("Al fin!");		
	}
}
